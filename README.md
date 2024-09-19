Klipper_wait_Tempreture.py Alters g-code to replace M109 S{} T{} commands to native klipper TEMPERATURE_WAIT command.
But because TEMPERATURE_WAIT needs SENSOR to be defined, Only M109 S{} is not replaced.
S parameter needs to be before T parameter.
SET_HEATER_TEMPERATURE is also added to gcode so temp is set like M109 does.
Also you can give script a hysteresis parameter, SET_HYSTERESIS= in start Gcode. If not defined, defaults to 1.
You can use it as M109, wait temp to rise and also to drop, use as is. To wait only raise, Comment out the corresponding line in the code.
