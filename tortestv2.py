#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Inputs: In1 = 27;  In2 = 29; In3 = 31; In4 = 33
# Outputs:  Out1 = 22; Out2  = 24; Out3 = 26; Out4 = 28

# Benoetigte Bibliotheken importieren
from time import sleep
import RPi.GPIO as gpio

# Pinbelegung auf BOARD setzten und nutzlose Warnungen deaktivieren
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

# setup pins.
# inputs definieren und Pins konfigurieren
input = [27, 29, 31, 33]
for i in range (4):
	gpio.setup(input[i], gpio.IN)
	
# outputs definieren und Pins konfigurieren
output = [22, 24, 26, 28]
for i in range (4):
	gpio.setup(output[i], gpio.OUT)
	
while True:
	for i in range (4):
		if gpio.input(input[i]) == gpio.HIGH:
			print ("Tor " + i + " ist offen.")
			gpio.output(output[i], gpio.HIGH)
		else:
			print ("Tor " + i + " ist zu.")
			gpio.output(output[i], gpio.HIGH)
			
		sleep(5)
			