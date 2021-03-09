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

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port=1
server_socket.bind(("", port))
server_socket.listen(1)

uuid = "837e6578-1497-11eb-adc1-0242ac120002"
bluetooth.advertise_service(server_socket, "3x3ledControl",
                  service_id = uuid,
                  service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
                  profiles = [ bluetooth.SERIAL_PORT_PROFILE ],
                  )

print("Waiting for connection on RFCOMM channel {}".format(server_socket.getsockname()[1]))
client_socket, address = server_socket.accept()
print("Accepted connection from ", address)

while True:
    try:
        data = client_socket.recv(1024)
        data = data.decode()

        data = data.replace(' ','')
        data = data.replace('\n','')
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
    except bluetooth.btcommon.BluetoothError:
        print("Connection lost, please reconnect")
        client_socket, address = server_socket.accept()
        print("Accepted connection from ", address)
        GPIO.cleanup()
        client_socket.close()
        server_socket.close()
    except Exception as e: #print(repr(e))
        traceback.print_exc()
