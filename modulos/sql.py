import sqlite3


class Datos:

    def __init__(self):
        super().__init__()

    @staticmethod
    def connexion():
        conn = sqlite3.connect("baseDatos/gestion.db")
        cursor = conn.cursor()

    @staticmethod
    def tancar_conn(self, conn, cursor):
        cursor.close()
        conn.close()

    # introduction, update and remove data from Clients.

    def dclientes(self):
        pass

    # introduction, update and remove data from Productes.
    def dproductos(self):
        pass

    # querys from data base.
    def dhistorial(self):
        pass

    # introduction, update and remove data from Cassos.
    def dcasos(self):
        pass

    # querys search
    def dbusqueda(self):
        pass
