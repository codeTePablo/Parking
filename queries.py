# user = Person
CREATE_TABLE_USER = "CREATE TABLE IF NOT EXISTS new_user (id SERIAL PRIMARY KEY, name TEXT, surname TEXT, num_cuenta INTEGER, num_placa TEXT);"

INSERT_TABLE_USER = "INSERT INTO new_user (name, surname, num_cuenta, num_placa) VALUES (%s, %s, %s, %s) RETURNING id;"


# guest = Guest
CREATE_TABLE_GUEST = "CREATE TABLE IF NOT EXISTS guest (folio SERIAL PRIMARY KEY, fecha DATE, hora TIME, password TEXT);"

INSERT_TABLE_GUEST = (
    "INSERT INTO guest (fecha, hora, password) VALUES (%s, %s, %s) RETURNING folio;"
)
