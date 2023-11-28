# user = Person
CREATE_TABLE_USER = "CREATE TABLE IF NOT EXISTS new_user (id SERIAL PRIMARY KEY, name TEXT, surname TEXT, num_cuenta INTEGER, num_placa TEXT, finger INTEGER, fecha DATE, hora TIME);"

INSERT_TABLE_USER = "INSERT INTO new_user (name, surname, num_cuenta, num_placa, finger) VALUES (%s, %s, %s, %s, %s) RETURNING id;"

SEARCH_USER_BY_FINGER = "SELECT * FROM new_user WHERE finger = %s;"

# INSERT_TIME = "INSERT INTO new_user (fecha, hora) VALUES (%s, %s) WHERE finger = %s;"
INSERT_TIME = "UPDATE new_user SET fecha = %s, hora = %s WHERE finger = %s;"


# guest = Guest
CREATE_TABLE_GUEST = "CREATE TABLE IF NOT EXISTS guest (folio SERIAL PRIMARY KEY, fecha DATE, hora TIME, finger INTEGER, exit_hour TIME, tax INTEGER);"

INSERT_TABLE_GUEST = (
    "INSERT INTO guest (fecha, hora, finger) VALUES (%s, %s, %s) RETURNING folio;"
)

SELECT_GUEST_BY_FINGER = "SELECT * FROM guest WHERE finger = %s;"

UPDATE_GUEST_BY_FINGER = (
    "UPDATE guest SET exit_hour = %s, tax = %s WHERE finger = %s RETURNING *;"
)


# admnin
SELECT_ALL = "SELECT * FROM new_user;"

SELECT_USER = "SELECT * FROM new_user WHERE id = %s;"

UPDATE_USER = "UPDATE new_user SET name = %s, surname = %s, num_cuenta = %s, num_placa = %s WHERE id = %s RETURNING *;"

DELETE_USER = "DELETE FROM new_user WHERE id = %s;"
