#!/usr/bin/python
import sys
import re
import os

sourceFile=sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()

destFile = re.sub('\\.gcode$','',sourceFile)

with open(destFile, "w") as of:
    #default hysteresis if not set in start gcode -> SET_HYSTERESIS=
    hyst = 1
    for lIndex in range(len(lines)):
        oline = lines[lIndex]
        # Parse gcode line
        parts = oline.split(';', 1)
        if len(parts) > 0:
            # Parse command
            command = parts[0].strip()

            if command:
                stringMatch = re.search ('^SET_HYSTERESIS=', command)
                if stringMatch:
                    numbers = re.findall(r'\d+', oline)
                    try:
                        hyst = int(numbers[0])
                    except:
                        pass
                    #else:
                        #print("hyst set")
                #Look for M109 S...  note that S parameter need to be before T parameter if use them in the custom gcodes
                stringMatch = re.search ('^M109 S(.*)', command)
                if stringMatch:
                    numbers = re.findall(r'\d+', oline)
                    #See if specific tool is called, if not, leave M109 as it is
                    try:
                        tool = numbers[2]
                    except:
                        pass
                        #print("no tool defined")
                    else:
                        if tool == "0":
                            tool = "extruder"
                        else:
                            tool = ("extruder%s" % tool)
                        temp = int(numbers[1])
                        #add set temp so we do the same as M109 does
                        of.write("SET_HEATER_TEMPERATURE HEATER=%s TARGET=%s ; set temperature\n" % (tool, temp))
                        
                        #Waits temp only to rise 
                        oline = ("TEMPERATURE_WAIT SENSOR=%s MINIMUM=%s ; and wait for it to be reached\n" % (tool, temp - hyst))
                        
                        #Also waits temp to drop, like M109 does, comment or uncomment as needed
                        #oline = ("TEMPERATURE_WAIT SENSOR=%s MINIMUM=%s MAXIMUM=%s ; and wait for it to be reached\n" % (tool, temp - hyst, temp + hyst))
                        
                       
            # Write original or altered line       
            of.write(oline)
of.close()
f.close()
