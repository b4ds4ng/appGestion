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

        datos = []
        cnx = Conexion.conexion()

        #for entrada in entradas:
        cursor= cnx.cursor()
        print(datos, entradas)
        """query = "INSERT INTO clients ( nom, cognom, email, tel, data,tract) VALUES ( ?, ?, ?, ?, ?,?)"
        cursor.execute(query, datos)
            #print(entrada)
        cnx.commit()
        cursor.close()"""
        cnx.close()

    def alta_producte(self):
        pass

    def alta_cassos(self):
        pass