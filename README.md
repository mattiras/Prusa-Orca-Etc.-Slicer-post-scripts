Klipper_wait_Tempreture.py Alters g-code to replace M109 Snnn Tn commands to native klipper TEMPERATURE_WAIT command. Useful to toolchanger printers, because you can add hysteresis as "forgiveness" to temp waits. Unnecessary waiting results oozing.

Because TEMPERATURE_WAIT needs SENSOR to be defined, M109 Snnn without Tn parameter in code is not replaced.
S parameter needs to be before T parameter.
SET_HEATER_TEMPERATURE is also added to gcode so temp is set like M109 does.
You can give script a hysteresis parameter, SET_HYSTERESIS= in start Gcode. If not defined, defaults to 1.
You can use it like M109, wait temp to rise and also to drop, use as is.
To wait only temp to raise, Comment out the corresponding line in the code.
