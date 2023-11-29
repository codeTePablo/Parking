import os
from contextlib import contextmanager
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv
from queries import *

load_dotenv()
database_uri = os.environ["DATABASE_URI"]

parking = SimpleConnectionPool(minconn=1, maxconn=10, dsn=database_uri)


@contextmanager
def get_connection():
    connection = parking.getconn()
    try:
        yield connection
    finally:
        parking.putconn(connection)


@contextmanager
def get_cursor(connection):
    with connection:
        with connection.cursor() as cursor:
            yield cursor


# USER
def create_tables(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_TABLE_USER)
        cursor.execute(CREATE_TABLE_GUEST)
        cursor.execute(CREATE_TABLE_PARKING)


def register_new_user(
    connection,
    name: str,
    surname: str,
    num_cuenta: int,
    num_placa: str,
    finger: int,
) -> int:
    with get_cursor(connection) as cursor:
        cursor.execute(
            INSERT_TABLE_USER, (name, surname, num_cuenta, num_placa, finger)
        )
        new_user = cursor.fetchone()[0]
        return new_user


def search_user_by_finger(connection, finger: int):
    with get_cursor(connection) as cursor:
        cursor.execute(SEARCH_USER_BY_FINGER, (finger,))
        user = cursor.fetchone()
        # print(user)
        return user


def update_user_id(connection, name, surname, num_cuenta, num_placa, idn):
    with get_cursor(connection) as cursor:
        cursor.execute(
            UPDATE_USER,
            (
                name,
                surname,
                num_cuenta,
                num_placa,
                idn,
            ),
        )
        connection.commit()
        return True


def detele_user(connection, id):
    with get_cursor(connection) as cursor:
        cursor.execute(DELETE_USER, (id,))
        connection.commit()
        return True


# insert hour and date
def insert_hour(connection, fecha, hora, finger):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_TIME, (fecha, hora, finger))
        connection.commit()
        return True


# GUEST
def create_table_guest(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_TABLE_GUEST)


def register_new_guest(connection, fecha, hora, finger):
    with get_cursor(connection) as cursor:
        cursor.execute(
            INSERT_TABLE_GUEST,
            (
                fecha,
                hora,
                finger,
            ),
        )
        guest_id = cursor.fetchone()[0]
        return guest_id


def get_guest_pass(connection, finger):
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_GUEST_BY_FINGER, (finger,))
        guest = cursor.fetchone()
        return guest


def update_guest_exit_time(connection, exit_time, tax, finger):
    with get_cursor(connection) as cursor:
        cursor.execute(
            UPDATE_GUEST_BY_FINGER,
            (
                exit_time,
                tax,
                finger,
            ),
        )
        guest = cursor.fetchone()
        # print(guest)
        return guest


def get_all_guests(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_ALL)
        guests = cursor.fetchall()
        return guests


def get_user(connection, id):
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_USER, (id,))
        user = cursor.fetchone()
        return user


def insert_into_parking(connection):
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_INTO_PARKING)
        parking_box = cursor.fetchone()[0]
        return parking_box


create_tables(parking.getconn())
