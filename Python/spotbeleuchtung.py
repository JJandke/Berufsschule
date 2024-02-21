#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
Tasterports = [2, 3, 4, 17, 27, 22, 10, 9]
LEDports = [14, 14, 23, 24, 25, 8, 7, 12]
dauer = 0.5

for i in Tasterports:
  GPIO.setup(i, GPIO.IN)
  
for i in LEDports:
  GPIO.setup(i, GPIO.OUT)
  
while True:
  for i in LEDports:
    GPIO.output(i, HIGH)
    time.sleep(dauer)
    GPIO.output(i, LOW)