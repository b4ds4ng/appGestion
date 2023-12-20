
class Clientes:

    def __init__(self, nom=None, cognom=None, email=None, tel=None, data=None, trac=None):
        super().__init__()
        self.id = None
        self.nombre = nom
        self.cognom = cognom
        self.email = email
        self.tel = tel
        self.data = data
        self.trac = trac

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

    def __init__(self):
        super().__init__()

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
