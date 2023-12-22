import sqlite3 as sq


class Conexion:

    def __init__(self):
        super().__init__()
        self.conexion()


    def conexion(self):

        base_datos = "baseDatos/gestion.db"
        conec = sq.connect(base_datos)
        return conec

    def alta(self, datos):

        conexion = self.conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO clientes (nom, cognom, email, tel, data, trac) values (?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()





