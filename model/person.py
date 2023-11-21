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
        _id: int = None,
    ):
        self.id = _id
        self.name = name
        self.surname = surname
        self.num_cuenta = num_cuenta
        self.num_placa = num_placa
        # self.finger = finger

    def save(self):
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
