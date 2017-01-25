# Light of Erandil!

A photoresistor is used to sense when the room becomes dark. When the room is dark an LED illuminates

## Items Needed

1) 2.2V LED
2) 330 Ohm Resistor
3) CDS Photocell (roughly 11k-650k)
4) 1uF capacitor

## Explanation

The photoresistor is connected to 3.3V on one side and a both a GPIO pin and the ground through a capacitor. The GPIO pin is digital, so it can only detect a high or low voltage. When the light is turned off the resistance is high and the capacitor charges slowly. I have the GPIO pin on the raspberry pi measure the time it takes the capacitor to charge. It's a really simple loop that basically sets the pin as an output to make the voltage near 0V, then it sets it as an input and counts how long it takes to reach high voltage. Then I just experimented to find an RC time that corresponds to "dark" and have another pin turn on an LED if its dark
