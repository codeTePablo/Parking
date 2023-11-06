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
    """
    Args:
        arg1 (str): connection to database
    Return:
        connection: this simplify so much to make connections, only we can call function
        and wait cursor to execute after of any transaction
    """
    with connection:
        with connection.cursor() as cursor:
            yield cursor


# USER
def create_tables(connection):
    """
    Args:
        arg1 (str): connection to database
    Return:
        Query: create polls
    """
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_TABLE_USER)
        cursor.execute(CREATE_TABLE_GUEST)


def register_new_user(
    connection, name: str, surname: str, num_cuenta: int, num_placa: str
) -> int:
    """create new user
    Args:
        arg1 (): connection database
        arg2 (str): name has user
        arg3 (str): surmane has user
        arg4 (str): num_cuenta has user
        arg5 (str): num_placa has user
    Return:
        Query: register new user
    """
    with get_cursor(connection) as cursor:
        cursor.execute(INSERT_TABLE_USER, (name, surname, num_cuenta, num_placa))
        new_user = cursor.fetchone()[0]
        return new_user


# GUEST
def create_table_guest(connection):
    """
    Args:
        arg1 (str): connection to database
    Return:
        Query: create polls
    """
    with get_cursor(connection) as cursor:
        cursor.execute(CREATE_TABLE_GUEST)


def register_new_guest(connection, fecha, hora, password):
    with get_cursor(connection) as cursor:
        cursor.execute(
            INSERT_TABLE_GUEST,
            (
                fecha,
                hora,
                password,
            ),
        )
        guest_id = cursor.fetchone()[0]
        return guest_id


def get_guest_pass(connection, password):
    with get_cursor(connection) as cursor:
        cursor.execute(SELECT_TABLE_GUEST, (password,))
        guest = cursor.fetchone()
        return guest


create_tables(parking.getconn())
