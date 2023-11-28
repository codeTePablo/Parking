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
        date: str = None,
        hour: str = None,
        finger: int = None,
        exit_time: str = None,
        tax: float = None,
    ):
        self.folio = folio
        self.date = date
        self.hour = hour
        self.tax = tax
        self.finger = finger
        self.exit_time = exit_time

    def save(self):
        with get_connection() as connection:
            new_guest = db.register_new_guest(
                connection, self.date, self.hour, self.finger
            )
            self.folio = new_guest

    def __repr__(self):
        return f"<People {self.name} {self.surname}>"

    def update_guest(self):
        with get_connection() as connection:
            guest = db.update_guest_exit_time(
                connection, self.exit_time, self.tax, self.finger
            )
            return guest

    def get_guest(self):
        with get_connection() as connection:
            guest = db.get_guest_pass(connection, self.finger)
            return guest
