import tkinter as tk


class Formularios(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        
    def form_clientes(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Clients", 
                                              font="Roboto", bg="white")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.lateral_derecho_label.pack(side="top", ipadx=350, ipady=10)

        print("Hola, vengo del fomulario")

    def form_productos(self):

        print("vengo de productos")

    def form_casos(self):

        print("vengo de cassos")

    def form_buscar(self):

        print("buscas algo!")

    def insertar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self):
        pass

    def cancelar(self):
        pass

    

