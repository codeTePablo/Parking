import serial

arduino_port = "COM5"  # Cambia esto al puerto correcto de tu Arduino
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)


def scan(command):
    # Espera a que Arduino se inicie
    ser.readline()

    while True:
        ser.write(command.encode())
        response = ser.readline().decode().strip()
        print("Respuesta de Arduino:", response)

    # ser.close()


def read(command):
    # Espera a que Arduino se inicie
    ser.readline()

    while True:
        ser.write(command.encode())
        response = ser.readline().decode().strip()
        print("Respuesta de Arduino:", response)

    # ser.close()


# scan("E")
read("R")
# read()
