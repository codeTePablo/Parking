import serial

arduino_port = "COM3"  # Cambia esto al puerto correcto de tu Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)


def scan(command):
    # Espera a que Arduino se inicie
    ser.readline()

    while True:
        ser.write(command.encode())
        response = ser.readline().decode().strip()
        print("Respuesta de Arduino:", response)
        if response.startswith("Enrolling ID"):
            break
        # if response == "Stored!":
        # break


def read(command):
    # Espera a que Arduino se inicie
    ser.readline()

    while True:
        ser.write(command.encode())
        response = ser.readline().decode().strip()
        print("Respuesta de Arduino:", response)
        # encontrar el ID en response
        id_finger = response[10:11]
        # print(type(id_finger))
        # si se toma una huella se debera de detener el programa
        if id_finger == "1":
            print("1")
            # ser.close()
            # break
        elif id_finger == "2":
            print("2")
            # break
        elif id_finger == "3":
            print("3")


# scan("E")
# read("R")
