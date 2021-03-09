import sys
import bluetooth
import RPi.GPIO as GPIO
import traceback

pin_dict = {"A1":21,
	"A2":20,
	"A3":16,
	"B1":12,
	"B2":26,
	"B3":19,
	"C1":13,
	"C2":6,
	"C3":5
    }

GPIO.setmode(GPIO.BCM)

for y in range (5,27):
	GPIO.setup(y,GPIO.OUT)
try:
	server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

	port = 1
	server_socket.bind(("",port))
	server_socket.listen(1)

	client_socket,address = server_socket.accept()
	print ("Accepted connection from ",address)

	while True:
		data = client_socket.recv(1024)
		data = data.decode()
		print(data)
        
        	# Mensaje recibido
		holds_list = data.split(',')
		print(holds_list)
		for x in range (5,27):
			GPIO.output(x,GPIO.LOW)
		for hold in holds_list:
			print(hold)
			led_pin = pin_dict[hold]
			print("Presa:", hold,", pin:", led_pin)
			GPIO.output(led_pin,GPIO.HIGH)


except Exception as e: #print(repr(e))
	traceback.print_exc()
finally:
	GPIO.cleanup()

