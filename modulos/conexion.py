import sqlite3 as sq
from tkinter import messagebox as msg



""" Recordar de fer tots els ifs controlant els errors, try-except"""


class Conexion:

    def __init__(self, formularios):
        super().__init__()
        self.formularios = formularios


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
        from .formularios import Formularios

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
            entradas = None
            campos = 0
            print("en elif 6", entradas)
            print(campos)
        # Aquí és processat el formulari dels productes.
        elif campos ==3:

            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO productes ( categoria, tractament, descripcio) VALUES ( ?, ?, ?)"
            cursor.execute(query, list(entradas))
            cnx.commit()
            cursor.close()
            cnx.close()
            msg.showinfo("productes", "Producte afegit correctament")
            Formularios.eliminar_lista_entradas(entradas)
            print("en elif 3", entradas)
            print("elif 3", campos)


        # Aquí és processat el formulari dels casos.
        elif campos  == 2:

            cnx = Conexion.conexion()
            cursor = cnx.cursor()
            query = "INSERT INTO casos ( tracta, descripcion) VALUES ( ?, ?)"
            cursor.execute(query, list(entradas))
            cnx.commit()
            cursor.close()
            cnx.close()
            msg.showinfo("cas", "Cas afegit correctament")
            Formularios.eliminar_lista_entradas(entradas)
            print("en elif 2", entradas)
            print("elif 2", campos)


        else:

            msg.showwarning("Error", "Alguna cosa no ha anat be")
            print("del else", entradas)
            print("del else", campos)


class Eliminar:
    """Aquesta classe elimina registres en la base de dades, de qualsevol formulari."""
    pass

class Actualizar:
    """Aquesta classe actualitza registres en la base de dades, de qualsevol formulari."""
    pass
