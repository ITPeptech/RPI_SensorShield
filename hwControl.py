'''
peptech GmbH

Authored By: 
Qais Sunna
Qais.Sunna@peptech.de
'''

import spidev
import RPi.GPIO as GPIO
from time import sleep

spi = spidev.SpiDev()
voltage = 5.2           #<----------------CHANGE THIS IF NECESSARY
MUX_A = 26
MUX_B = 19
MUX_C = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(MUX_A,GPIO.OUT)
GPIO.setup(MUX_B,GPIO.OUT)
GPIO.setup(MUX_C,GPIO.OUT)

def openSPI():
    spi.open(0,0)
    spi.mode = 0
    spi.max_speed_hz = int(1e6) # 1 MHz 

def closeSPI():
    spi.close()

def readADC101():
    #Texas Instrument ADC101S021CIMF 10Bit
    reading = spi.readbytes(2)
    hi = reading[0] & 0x1f
    lo = reading[1] & 0xf8
    return (hi<<6) + (lo>>2)

def chooseSensor(sensor):   #Switch Mux pins according to the sensor number
    bits = (format(sensor, "03b"))
    S2,S1,S0 = int(bits[0]),int(bits[1]),int(bits[2])
    GPIO.output(MUX_A,S0)
    GPIO.output(MUX_B,S1)
    GPIO.output(MUX_C,S2)
    sleep(1e-2)