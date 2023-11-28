import psycopg2

from db import get_connection
import db


class Person:
    def __init__(
        self,
        # finger,  # esria sacar el finger id desde el arduino
        name: str,
        surname: str,
        num_cuenta: int,
        num_placa: str,
        finger: int = None,
        fecha: str = None,
        hora: str = None,
        _id: int = None,
    ):
        self.id = _id
        self.name = name
        self.surname = surname
        self.num_cuenta = num_cuenta
        self.num_placa = num_placa
        self.finger = finger
        self.fecha = fecha
        self.hora = hora

    def save(self):
        with get_connection() as connection:
            new_user = db.register_new_user(
                connection,
                self.name,
                self.surname,
                self.num_cuenta,
                self.num_placa,
                self.finger,
            )
            self.id = new_user

    def search_by_finger(self):
        with get_connection() as connection:
            user = db.search_user_by_finger(connection, self.finger)
            # print(user)
            return user

    def insert_hour(self, fecha, hora, finger):
        with get_connection() as connection:
            guest_id = db.insert_hour(connection, fecha, hora, finger)
            return guest_id

    def __repr__(self):
        return f"<People {self.name} {self.surname}>"
