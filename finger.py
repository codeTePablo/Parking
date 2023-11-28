import serial
import time

# Abre la conexión con el puerto serie. Ajusta el puerto COM según tu configuración.
arduino_port = "COM3"
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)


def enroll_fingerprint(id):
    ser.readline()
    while True:
        response = ser.readline().decode().strip()
        print(response)
        # Envia el comando 'E' para enrollar huella en el Arduino
        ser.write(b"E")
        time.sleep(
            0.1
        )  # Espera un tiempo suficiente para que Arduino complete la operación

        # Envía el ID
        ser.write(str(id).encode())
        time.sleep(0.1)  # Espera a que el Arduino procese el ID
        if response == "Stored!":
            # ser.close()
            break


def read_fingerprint():
    while True:
        ser.write(b"R")
        time.sleep(0.1)
        response = ser.readline().decode().strip()
        print(f"{response}")

        # Verifica si la respuesta contiene "Found ID #"
        if "Found ID #" in response:
            # Encuentra la posición de "Found ID #"
            start_index = response.find("Found ID #")

            # Extrae el número después de "Found ID #"
            id_str = response[start_index + len("Found ID #") :].split()[0]

            # Convierte el número a entero
            fingerprint_id = int(id_str)

            print(f"Fingerprint ID: {fingerprint_id}")
            # ser.close()
            return fingerprint_id


# Ejemplo de uso
# read_fingerprint()

# Enrollar huella
# enroll_fingerprint()

# Leer huella
# read_fingerprint()

# Cierra la conexión con el puerto serie
# ser.close()
