# Simple demo of setting the DAC value up and down through its entire range
# of values.
# Author: Tony DiCola
import board
import busio
import math
from time import sleep

import adafruit_mcp4725


# Initialize I2C bus.
i2c = busio.I2C(board.SCL, board.SDA, frequency=4000)

# Initialize MCP4725.
dac = adafruit_mcp4725.MCP4725(i2c)
# Optionally you can specify a different addres if you override the A0 pin.
# amp = adafruit_max9744.MAX9744(i2c, address=0x63)

# There are a three ways to set the DAC output, you can use any of these:
dac.value = 65535  # Use the value property with a 16-bit number just like
# the AnalogOut class.  Note the MCP4725 is only a 12-bit
# DAC so quantization errors will occur.  The range of
# values is 0 (minimum/ground) to 65535 (maximum/Vout).

dac.raw_value = 4095  # Use the raw_value property to directly read and write
# the 12-bit DAC value.  The range of values is
# 0 (minimum/ground) to 4095 (maximum/Vout).

dac.normalized_value = 1.0  # Use the normalized_value property to set the
# output with a floating point value in the range
# 0 to 1.0 where 0 is minimum/ground and 1.0 is
# maximum/Vout.

# Main loop will go up and down through the range of DAC values forever.

t =0.0
while True:
    
    '''
    wave1 = int(1023* math.sin(2*math.pi*1*t) + 2047)
    wave2 = int(512* math.sin(2*math.pi*2*t) + 2047)
'''

    wave1 = (math.sin(2*math.pi*1*t))
    wave2 = (0.5*math.sin(2*math.pi*3*t))
    wave3 = (0.25*math.sin(2*math.pi*4*t))
    dac.raw_value = int((512*( wave1 + wave2+wave3))+2048)

    t= t +0.01
    sleep(0.01)