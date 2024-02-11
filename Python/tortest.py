#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Inputs: In1 = 27;  In2 = 29; In3 = 31; In4 = 33
# Outputs:  Out1 = 22; Out2  = 24; Out3 = 26; Out4 = 28

from time import sleep
# import logging
import RPi.gpio as gpio

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

# setup pins.
gpio.setup(27, gpio.IN)  # Tor1
gpio.setup(29, gpio.IN)  # Tor2
gpio.setup(31, gpio.IN)  # Tor3
gpio.setup(33, gpio.IN)  # Tor4

gpio.setup(22, gpio.OUT)  # StatusLED1
gpio.setup(24, gpio.OUT)  # StatusLED2
gpio.setup(26, gpio.OUT)  # StatusLED3
gpio.setup(28, gpio.OUT)  # StatusLED4

while True:
    # Tor1
    if gpio.input(27) == gpio.HIGH:
        print("Tor1 ist offen")
        gpio.output(22, gpio.HIGH)
    else:
        print("Tor1 ist zu")
        gpio.output(22, gpio.LOW)

    # Tor2
    if gpio.input(29) == gpio.HIGH:
        print("Tor2 ist offen")
        gpio.output(24, gpio.HIGH)
    else:
        print("Tor2 ist zu")
        gpio.output(24, gpio.LOW)

    # Tor3
    if gpio.input(31) == gpio.HIGH:
        print("Tor2 ist offen")
        gpio.output(26, gpio.HIGH)
    else:
        print("Tor2 ist zu")
        gpio.output(26, gpio.LOW)

    # Tor4
    if gpio.input(33) == gpio.HIGH:
        print("Tor4 ist offen")
        gpio.output(28, gpio.HIGH)
    else:
        print("Tor4 ist zu")
        gpio.output(28, gpio.LOW)

    # 5s warten, damit die Konsole übersichtlich bleibt
    sleep(5)
