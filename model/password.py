# crea un programa para generar contraseñas aleatorias de 4 caracteres

import random


class Password:
    def generar_contrasena(self):
        # mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeros = "0123456789"

        contrasena = []

        for i in range(4):
            caracter_random = random.choice(numeros)
            contrasena.append(caracter_random)

        contrasena = "".join(contrasena)
        # print(contrasena)
        # contraseña tipo
        # print(type(contrasena))
        return contrasena


# password = Password
# password.generar_contrasena()
