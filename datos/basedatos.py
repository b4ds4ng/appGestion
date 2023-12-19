from tkinter import messagebox
from appGestion.datos.sql import Conexion


class Clientes:

    def __init__(self, nom, cognom, email, tel, data, trac):
        super().__init__()
        self.id = None
        self.nombre = nom
        self.cognom = cognom
        self.email = email
        self.tel = tel
        self.data = data
        self.trac = trac

    def __str__(self):
        return f"gclientes[{self.nombre}, {self.cognom}, {self.email}, {self.tel}, {self.data}, {self.trac}]"

    def gclientes(self, nom, cognom, email, tel, data, trac):
        conexion = Conexion()
        conexion.cursor()
        conexion.tancar_conn()
        self.nombre = nom
        self.cognom = cognom
        self.email = email
        self.tel = tel
        self.data = data
        self.trac = trac

        sql = f""" INSERT INTO  clientes (nom, cognom, email, tel, data, trac
               VALUES ('{self.nombre}', '{self.cognom}', '{self.email}',
                '{self.tel}', '{self.data}', '{self.trac}"""

        try:
            conexion.cursor.execute(sql)
            conexion.tancar_conn()
        except conexion:
            messagebox.showwarning("Error de connexió", "Torna-ho a provar")

    def rclientes(self):

        pass


class Productos:

    def __init__(self):

        super().__init__()

    def gproductos(self):
        pass

    def rproductos(self):
        pass


class Cassos:

    def gcasos(self):
        pass

    def rcasos(self):
        pass


class Historial:

    def mhistorial(self):
        pass


class Busqueda:

    def dbusqueda(self):
        pass
