import sqlite3 as sq
from tkinter import messagebox as msg





""" Recordar de fer tots els ifs controlant els errors, try-except"""


class Conexion:

    def __init__(self):
        super().__init__()


    @staticmethod
    def conexion():

        base_datos = "baseDatos/gestion.db"
        conec = sq.connect(base_datos)
        return conec


class Altas:
    """Aquesta classe processa els diferents formularis, clients, productes i casos. En funció de la
             quantitat de registres que són passats des de "formularios" a on són creats de forma dinàmica."""

    def __init__(self):
        super().__init__()


    @staticmethod
    def alta_cliente(entradas):

        # Aquí es processa el formulari de clients.
        campos = len(entradas)
        if campos  == 6:
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO clients ( nom, cognom, email, tel, data,tract) VALUES ( ?, ?, ?, ?, ?,?)"
            cursor.execute(query, entradas)
            cnx.commit()
            cursor.close()
            cnx.close()
            msg.showinfo("Clients", "Client afegit correctament")

        # Aquí és processat el formulari dels productes.
        elif campos ==3:
            print("campos 3", entradas)
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO productes ( categoria, tractament, descripcio) VALUES ( ?, ?, ?)"
            cursor.execute(query, list(entradas))
            cnx.commit()
            cursor.close()
            cnx.close()
            msg.showinfo("productes", "Producte afegit correctament")

        # Aquí és processat el formulari dels casos.
        elif campos  == 2:
            print("campos 2", entradas)
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO casos ( tracta, descripcion) VALUES ( ?, ?)"
            cursor.execute(query, list(entradas))
            cnx.commit()
            cursor.close()
            cnx.close()
            msg.showinfo("cas", "Cas afegit correctament")

        else:
            msg.showwarning("Error", "Alguna cosa no ha anat be")



class Eliminar:
    """Aquesta classe elimina registres en la base de dades, de qualsevol formulari."""
    pass

class Actualizar:
    """Aquesta classe actualitza registres en la base de dades, de qualsevol formulari."""
    pass
