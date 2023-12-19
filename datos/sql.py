import sqlite3 as sq


class Conexion:

    def __init__(self):
        self.base_datos = "baseDatos/gestion.db"
        self.conec = sq.connect(self.base_datos)
        self.cursor = self.conec.cursor()

    def tancar_conn(self):
        self.conec.commit()
        self.conec.close()
