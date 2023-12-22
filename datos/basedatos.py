from appGestion.datos.conexion import Conexion


class Clientes:

    def __init__(self):
        super().__init__()
        self.ingresado = Conexion()

    def rclientes(self, *args):

        for idx, (datos) in enumerate(args):
            datos.get = f"{datos}"
            self.ingresado.alta(datos)
            datos.set(datos)
            datos.execute(datos)
            Conexion()

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
