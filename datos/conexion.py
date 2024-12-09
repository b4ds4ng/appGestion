import sqlite3 as sq




class Conexion:

    def __init__(self):
        super().__init__()

        self.entradas = []

    @staticmethod
    def conexion():

        base_datos = "baseDatos/gestion.db"
        conec = sq.connect(base_datos)
        return conec


    @staticmethod
    def alta_cliente(entradas):
        campos = len(entradas)
        if campos == 6:
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO clients ( nom, cognom, email, tel, data,tract) VALUES ( ?, ?, ?, ?, ?,?)"
            cursor.execute(query, entradas)
            cnx.commit()
            cursor.close()
            cnx.close()

        elif campos == 3:
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO productes ( categoria, tractament, descripcio) VALUES ( ?, ?, ?)"
            cursor.execute(query, entradas)
            cnx.commit()
            cursor.close()
            cnx.close()

        elif campos == 2:
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO casos ( tracta, descripcion) VALUES ( ?, ?)"
            cursor.execute(query, entradas)
            cnx.commit()
            cursor.close()
            cnx.close()

        else:
            print("No arriba res")


    def alta_producte(self):
        pass

    def alta_cassos(self):
        pass