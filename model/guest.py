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
        exit_time: str = None,
        tax: float = None,
    ):
        self.folio = folio
        self.fecha = fecha
        self.hora = hora
        self.password = password
        self.exit_time = exit_time
        self.tax = tax

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

    def update_guest(self, exit_time, tax, password):
        with get_connection() as connection:
            guest = db.update_guest_exit_time(
                connection,
                exit_time,
                tax,
                password,
            )
            return guest

    def calculate_tax(self, hora, exit_time, tax):
        with get_connection() as connection:
            tax = db.calculate_tax_price(connection, hora, exit_time, tax)
            return tax
