# This program will turn on an LED in low light conditions

import RPi.GPIO as GPIO
import time

#Setup the GPIO as BCM numbering
GPIO.setmode(GPIO.BCM)

#Define pin to circuit
pin_to_circuit = 4
pin_to_led = 17

#Setup led pin as an input
GPIO.setup(pin_to_led, GPIO.OUT)

def rc_time(pin_to_circuit):
    count = 0
    
    #Output on the pin for 10ms
    GPIO.setup(pin_to_circuit,GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change pin to an input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    #Count until the pin goes to high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    return count    

#catcg wgeb script is interuppted, cleanup correctly
try:
    #main loop
    while True:
        lightval = rc_time(pin_to_circuit)
        print(lightval)
        #turn on led in the dark
        if lightval >= 2500:
            GPIO.output(pin_to_led, True)
        else:
            GPIO.output(pin_to_led, False)
            
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
