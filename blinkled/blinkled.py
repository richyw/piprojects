#This program will blink an LED 20 times.
# An LED and a 330R resistor should be hooked up in series between the GPIO17 pin and a ground pin

import RPi.GPIO as GPIO #import gpio library
import time #import time library

#setup the gpio as bcm numbering
GPIO.setmode(GPIO.BCM)

#disablewarnings
GPIO.setwarnings(False)

#setup gpio pin
GPIO.setup(17, GPIO.OUT)

# function to blink led
def blink_led():
    GPIO.output(17,True) #turn on LED
    time.sleep(0.5) #susepend the current thread for 1/2 second
    GPIO.output(17,False) #turn off the LED
    time.sleep(0.5) #suspend the current thread for 1/2 second

#blink the led 20 times
for i in range(0,20):
    blink_led()
    


