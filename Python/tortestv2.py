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

#GPIO Eingänge und Ausgänge festlegen
inputs = [27,29,31,33] 
outputs = [22,24,26,28]

for value in inputs: 
  gpio.setup(value, gpio.IN)
  
for value in outputs: 
  gpio.setup(value, gpio.OUT)


#GPIOS: Eingänge abfragen und Zustände optisch ausgeben
while True: 
  for i in range(len(inputs)): #Zählergesteuerte Schleife für Anzahl der Elemente 
    if gpio.input(inputs[i]) == gpio.HIGH: #Falls Spannung auf Input am Index i
      gpio.output(outputs[i], gpio.HIGH) #Gebe Spannung auf Output am Index i
    else:
        gpio.output(outputs[i], gpio.LOW)
        
  sleep(5)
 