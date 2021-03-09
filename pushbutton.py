import time
import RPi.GPIO as GPIO

buttonpin = 3 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

wasHigh = True
while True:
	if GPIO.input(buttonpin) == False and wasHigh:
		print("Button pushed!")
		wasHigh = False
		time.sleep(0.5)
	else:
		wasHigh = True
