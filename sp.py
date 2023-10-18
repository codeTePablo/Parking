import serial
import time

# Abre el puerto serie
ser = serial.Serial("COM3", 115200)

# Envía datos
ser.write(b"hello\\r\\n")

# Espera un poco para que el ESP32 pueda responder
time.sleep(1)

# Lee los datos recibidos
data = ser.readline()

print(data)
