import psycopg2
import datetime

from db import get_connection
import db


from datetime import datetime


class Guest:
    def __init__(self, name, arrival_time=None):
        self.name = name
        self.arrival_time = arrival_time if arrival_time else datetime.now()
        self.departure_time = None

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
            new_guest = db.create_people(connection, self.finger)
            self.id = new_guest

    def __repr__(self):
        return f"<People {self.name} {self.surname}>"

    def save_to_db(self):
        # Aquí va el código para guardar el nombre del invitado y la hora de llegada en la base de datos
        pass

    def set_departure_time(self, departure_time=None):
        self.departure_time = departure_time if departure_time else datetime.now()
        # Aquí puedes agregar el código para actualizar la hora de salida en la base de datos

    def get_stay_duration(self):
        if self.departure_time:
            duration = self.departure_time - self.arrival_time
            return duration
        else:
            return None
