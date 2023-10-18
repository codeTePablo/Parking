import serial

# from Adafruit_Fingerprint import Adafruit_Fingerprint

# Configura el puerto serie
ser = serial.Serial("COM3", 9600)

# Configura el sensor de huellas dactilares
finger = Adafruit_Fingerprint(ser)


def registrar_huella(id_usuario):
    print("Por favor, coloca tu dedo en el sensor...")
    while finger.getImage() != FINGERPRINT_OK:
        pass  # Espera a que se coloque el dedo
    print("Huella capturada")

    # Convierte la imagen en una plantilla
    if finger.image2Tz(1) != FINGERPRINT_OK:
        return False

    # Almacena la plantilla en la base de datos con el id del usuario
    if finger.storeModel(id_usuario) != FINGERPRINT_OK:
        return False

    return True


def verificar_huella():
    print("Por favor, coloca tu dedo en el sensor...")
    while finger.getImage() != FINGERPRINT_OK:
        pass  # Espera a que se coloque el dedo
    print("Huella capturada")

    # Convierte la imagen en una plantilla
    if finger.image2Tz(1) != FINGERPRINT_OK:
        return False

    # Busca la huella en la base de datos
    result = finger.fingerSearch()

    if result[0] == FINGERPRINT_OK:
        print(f"Huella encontrada con ID: {result[1]}")
        return result[1]  # Devuelve el ID del usuario
    else:
        print("Huella no encontrada")
        return None


if __name__ == "__main__":
    id_usuario = 1  # Ajusta esto según tus necesidades
    if registrar_huella(id_usuario):
        print("Huella registrada con éxito")
    else:
        print("Error al registrar la huella")

    id_verificado = verificar_huella()
    if id_verificado is not None:
        print(f"Usuario verificado con ID: {id_verificado}")

# Suponiendo que 'finger' es una instancia de Adafruit_Fingerprint
if finger.fingerFastSearch() == Adafruit_Fingerprint.OK:
    print("Huella encontrada!")
    print("ID: " + str(finger.fingerID))
else:
    print("Huella no encontrada")
