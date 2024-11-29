import sqlite3 as sq


class Conexion:

    def __init__(self, nom=None, cognom=None, email=None, tel=None, data=None, trac=None):
        super().__init__()
        self.nom = nom
        self.cognom = cognom
        self.email = email
        self.tel = tel
        self.data = data
        self.trac = trac
        self.entradas = []
    @staticmethod
    def conexion():

        base_datos = "baseDatos/gestion.db"
        conec = sq.connect(base_datos)
        return conec

    def alta_cliente(self, nom, cognom, email, tel, data, trac):
        cnx = self.conexion()
        cursor= cnx.cursor()
        query = "INSERT INTO clients ( nom, cognom, email, tel, data, trac) VALUES ( %s, %s, %s, %s, %s, %s)"
        cursor.execute(query,( nom, cognom, email, tel, data, trac))
        cnx.commit()
        cursor.close()
        cnx.close()

