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
            del campos
        # Aquí és processat el formulari dels productes.
        elif campos  == 3:
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO productes ( categoria, tractament, descripcio) VALUES ( ?, ?, ?)"
            cursor.execute(query, entradas)
            cnx.commit()
            cursor.close()
            cnx.close()
            msg.showinfo("productes", "Producte afegit correctament")
            print("conexion", entradas)
            del  campos


        # Aquí és processat el formulari dels casos.
        elif campos  == 2:
            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO casos ( tracta, descripcion) VALUES ( ?, ?)"
            cursor.execute(query, entradas)
            cnx.commit()
            cursor.close()
            cnx.close()
            msg.showinfo("cas", "Cas afegit correctament")
            print("conexion", entradas)
            del campos



        else:
            msg.showwarning("Error", "Alguna cosa no ha anat be")
            print(entradas)

    """"@staticmethod
    def eliminar_entrys(entradas):
        entradas = entradas    
        del entradas"""
    @staticmethod
    def vaciar_lista(entradas):

        campos = len(entradas)
        if campos == 6:
            del entradas[0:6]

        campos = len(entradas)
        if campos == 3:
            del entradas[0:3]

        campos = len(entradas)
        if campos == 2:
            del entradas[0:2]



class Eliminar:
    pass

class Actualizar:
    pass
