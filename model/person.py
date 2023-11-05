import psycopg2

from db import get_connection
import db


class Person:
    # aqui inclui el finger, por lo que las consultas en la db no funcionan
    def __init__(
        self,
        # finger,  # esria sacar el finger id desde el arduino
        name: str,
        surname: str,
        num_cuenta: int,
        num_placa: str,
        _id: int = None,
    ):
        """
        Args:
            arg1 (str): title of the poll
            arg1 (str): owner of the poll
            arg1 (int): id of the poll this database will generate automatically
        Return:
            self: parameters option_text, id, poll_id
        """
        self.id = _id
        self.name = name
        self.surname = surname
        self.num_cuenta = num_cuenta
        self.num_placa = num_placa
        # self.finger = finger

    def save(self):
        """
        Save new poll
        Args:
            arg1 (self): self class
        Return:
            Query: create new poll inside in database and this self.id will be
            this new poll
        """
        with get_connection() as connection:
            new_user = db.register_new_user(
                connection,
                self.name,
                self.surname,
                self.num_cuenta,
                self.num_placa,
            )
            self.id = new_user

    def __repr__(self):
        return f"<People {self.name} {self.surname}>"


# class Persona:
#     # la idea de este codigo es que tenemos que tener un
#     # ruta imagen desde el arduino y mandar la ruta a la base de datos

#     def __init__(self, nombre, ruta_imagen):
#         self.nombre = nombre
#         self.ruta_imagen = ruta_imagen

#     def obtener_imagen(self):
#         with open(self.ruta_imagen, "rb") as f:
#             imagen = f.read()
#         return imagen


# # ver la ruta en la que se guardan las imagenes del arduino
# persona1 = Persona("Juan", "/ruta/a/la/imagen/juan.png")
# imagen_juan = persona1.obtener_imagen()
