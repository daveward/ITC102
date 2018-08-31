# -*- coding: utf-8 -*-
"""

@author: David Ward
@title: Temperature Control Script For ITC102 device.

"""

import time
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
GPIO.output(32, GPIO.HIGH) ## PIN A13, TEC = ON
GPIO.setup(18, GPIO.OUT)   
GPIO.output(18, GPIO.LOW) ## PIN A12, TEC = ON

import Adafruit_MCP4725

# Create an instance of the DAC
# If more than one DAC in use on the board
# Modify the parameters below by using the respective I2C addresses
# Adafruit_MCP4724.MCP4725(address = 0x55, busnum=1)

dac = Adafruit_MCP4724.MCP4725()

print ('Press Ctrl+C to quit')
try:
    for i in range(0,1500, 50):
        dac.set_voltage(i)
        print ("Voltage step: ", i)
        time.sleep(5.0) # Wait for 5 seconds so we can see the change on the display
except KeyboardInterrupt: # On CTRL + C, clean up the GPIO ports and gracefully quit
    print (" ")
    print ("Powering TEC off and quitting")
    print (" ")
    GPIO.cleanup()
    sys.exit()
    
GPIO.cleanup()


