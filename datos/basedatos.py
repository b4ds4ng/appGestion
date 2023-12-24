from appGestion.datos.conexion import Conexion


class Clientes:

    def __init__(self, nom=None, cognom=None, email=None, tel=None, data=None, trac=None):
        super().__init__()
        self.ingresado = Conexion()
        self.nom = nom
        self.cognom = cognom
        self.email = email
        self.tel = tel
        self.data = data
        self.trac = trac
        self.entradas = None

    def rclientes(self, *args):

        for dato in args:
            self.entradas.append((dato.get()))
            print(f"datos recibidos: {dato.get}")

    def bclientes(self, *args):
        pass


class Productos:

    def __init__(self):

        super().__init__()

    def gproductos(self):
        pass

    def bproductos(self):
        pass


class Cassos:

    def __init__(self):
        super().__init__()

    def gcasos(self):
        pass

    def bcasos(self):
        pass


class Historial:

    def mhistorial(self):
        pass


class Busqueda:

    def dbusqueda(self):
        pass
