import sqlite3 as sq


class Conexion:

    def __init__(self, nom=None, cognom=None, email=None, tel=None, data=None, trac=None):
        super().__init__()
        self.conexion()
        self.nom = nom
        self.cognom = cognom
        self.email = email
        self.tel = tel
        self.data = data
        self.trac = trac
        self.conexion()

    def conexion(self):

        base_datos = "baseDatos/gestion.db"
        conec = sq.connect(base_datos)
        return conec

    def alta(self, *args):

        conexion = self.conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO clients (nom, cognom, email, tel, data, tract) values (?,?,?,?,?,?)"
        cursor.execute(sql, args)
        conexion.commit()
        conexion.close()
