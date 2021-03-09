import sys
import bluetooth
import RPi.GPIO as GPIO

try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16,GPIO.OUT)

	server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
	port = 1
	server_socket.bind(("",port))
	server_socket.listen(1)
 
	client_socket,address = server_socket.accept()
	print ("Accepted connection from ",address)

	while 1:
		data = client_socket.recv(1024)
		print(data)
		if data.isdigit():
			if int(data) == 1:
		    	        GPIO.output(16, GPIO.HIGH)
			elif int(data) == 0:
				GPIO.output(16,GPIO.LOW)
			else:
				print("Comando desconocido")
except:
    	print("Unexpected error:", sys.exc_info())
finally:
        GPIO.cleanup()

