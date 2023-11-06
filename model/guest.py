import psycopg2
import datetime
import random

from db import get_connection
import db


from datetime import datetime


class Guest:
    def __init__(
        self,
        folio: int = None,
        fecha: str = None,
        hora: str = None,
        password: str = None,
    ):
        self.folio = folio
        self.fecha = fecha
        self.hora = hora
        self.password = password

    def save(self):
        with get_connection() as connection:
            new_guest = db.register_new_guest(
                connection, self.fecha, self.hora, self.password
            )
            self.folio = new_guest

    def __repr__(self):
        return f"<People {self.name} {self.surname}>"

    def get_guest(self, password):
        with get_connection() as connection:
            guest = db.get_guest_pass(connection, password)
            return guest

    def set_departure_time(self, departure_time=None):
        self.departure_time = departure_time if departure_time else datetime.now()
        # Aquí puedes agregar el código para actualizar la hora de salida en la base de datos

    def get_stay_duration(self):
        if self.departure_time:
            duration = self.departure_time - self.arrival_time
            return duration
        else:
            return None
