import bluetooth

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1)

uuid = "e8e10f95-1a70-4b27-9ccf-02010264e9c8"
bluetooth.advertise_service(server_socket, "HackingChat",
                  service_id = uuid,
                  service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
                  profiles = [ bluetooth.SERIAL_PORT_PROFILE ], 
                  )

print("Waiting for connection on RFCOMM channel {}".format(server_socket.getsockname()[1]))
client_socket, address = server_socket.accept()
print("Accepted connection from ", address)

while(1):
	try:
		data = client_socket.recv(1024)
		print("Received: {}".format(data))
		if data == "q": #Write q to quit program
			print("Quitting...")
			break
	except bluetooth.btcommon.BluetoothError:
		print("Connection lost, please reconnect")
		client_socket, address = server_socket.accept()
		print("Accepted connection from ", address)
client_socket.close()
server_socket.close()
