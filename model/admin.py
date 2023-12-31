from db import get_connection
import db


class Admin:
    def __init__(self) -> None:
        pass

    def get_data(self):
        with get_connection() as connection:
            data = db.get_all_guests(connection)
            # print(data)
            return data

    def get_user(self, id):
        with get_connection() as connection:
            user = db.get_user(connection, id)
            # print(user)
            return user

    def update_user(self, name, surname, num_cuenta, num_placa, id):
        with get_connection() as connection:
            user = db.update_user_id(
                connection, name, surname, num_cuenta, num_placa, id
            )
            return user

    def drop_user(self, id):
        with get_connection() as connection:
            db.detele_user(connection, id)
