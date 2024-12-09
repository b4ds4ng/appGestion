import sqlite3 as sq



""" Recordar de fer tots els ifs controlant els errors, try-except"""


class Conexion:

    def __init__(self):
        super().__init__()

        self.entradas = []




    @staticmethod
    def conexion():
        """Aquesta funció processa els diferents formularis, clients, productes i casos. En funció de la
         quantitat de registres que són passats des de "formularios" a on són creats de forma dinàmica."""
        base_datos = "baseDatos/gestion.db"
        conec = sq.connect(base_datos)
        return conec


    @staticmethod
    def alta_cliente(entradas):
        campos = len(entradas)
        #Aquí es processa el formulari de clients.
        if campos == 6:
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO clients ( nom, cognom, email, tel, data,tract) VALUES ( ?, ?, ?, ?, ?,?)"
            cursor.execute(query, entradas)
            cnx.commit()
            cursor.close()
            cnx.close()

        # Aquí és processat el formulari dels productes.
        elif campos == 3:
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO productes ( categoria, tractament, descripcio) VALUES ( ?, ?, ?)"
            cursor.execute(query, entradas)
            cnx.commit()
            cursor.close()
            cnx.close()

        # Aquí és processat el formulari dels casos.
        elif campos == 2:
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO casos ( tracta, descripcion) VALUES ( ?, ?)"
            cursor.execute(query, entradas)
            cnx.commit()
            cursor.close()
            cnx.close()




        else:

            print("massa camps, els camps es sumen", campos)

    """@staticmethod
    def eliminar_entrys(entradas):
         entradas = []"""


