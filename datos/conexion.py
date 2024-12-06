import sqlite3 as sq


class Conexion:

    def __init__(self, *args):
        super().__init__()

        self.entradas = []

    @staticmethod
    def conexion():

        base_datos = "baseDatos/gestion.db"
        conec = sq.connect(base_datos)
        return conec

    def alta_cliente(self, *entradas):
        print("llega algo")
        print("datos: ", entradas)
        datos = []
        cnx = self.conexion()
        cursor= cnx.cursor()
        query = "INSERT INTO clients ( nom, cognom, email, tel, data, trac) VALUES ( %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, datos)
        cnx.commit()
        cursor.close()
        cnx.close()

    def alta_producte(self):
        pass

    def alta_cassos(self):
        pass