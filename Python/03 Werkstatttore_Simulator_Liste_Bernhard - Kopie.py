#Version 1.0
#Erstellt am: 06.07.2021
#Ersteller: Rol
#Zweck: Werkstatttorüberwachung mit LED Ausgabe.

# Import von Modulen
import RPi.GPIO as GPIO
import time

# Board Modus festlegen
GPIO.setmode(GPIO.BOARD)

# Festlegen der In- und Output Pins
Inputs = [3, 5, 7, 11] #Alternativ als Tupel Inputs = (3, 5, 7, 11)
Outputs = [8 , 10, 16, 18]

# Initialisierung der In- und Outpotnummerierungen
for value in Inputs:
GPIO.setup(value, GPIO.IN)
for value in Outputs:
GPIO.setup(value, GPIO.OUT)

# Status (offen/geschlossen) der Werkstattore ausgeben
while True:
for i in range(len(Inputs)):
if (GPIO.Input(Inputs[i]) == GPIO.HIGH):
GPIO.output(Outputs[i], GPIO.HIGH)
else :
GPIO.output(Outputs[i], GPIO.LOW)
time.sleep(1)