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

    def conexion(self):

        base_datos = "baseDatos/gestion.db"
        conec = sq.connect(base_datos)
        return conec

    def alta_cliente(self, *args: str):
        for dato in args:
            self.entradas.append(dato)
            lista = ''.join(str(x) for x in self.entradas)
            print(lista)

    def __str__(self) -> str:
        str_con_el_resultado = 'Datos: '
        for dato in self.entradas:
            str_con_el_resultado += "\n  * {}".format(dato)
        return str_con_el_resultado
