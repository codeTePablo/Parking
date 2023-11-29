from db import get_connection
import db


class Box:
    def __init__(self) -> None:
        pass

    def get_box(self):
        with get_connection() as connection:
            box = db.insert_into_parking(connection)
            # print(box)
            return box


# llamar a get_box() para obtener el numero de caja
# Box.get_box()
