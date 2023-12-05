import tkinter as tk
from tkinter import ttk, font




class Formularios(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        
        
    def form_clientes(self):

        # Create frame, label
        
        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Clients", 
                                              font="Roboto", bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

        # Create entrys and labels
       
        self.nombre = tk.Label(self.lateral_derecho, text="Nom", bg="white", font=("Roboto", 11,"bold"))
        self.entrada = tk.Entry(self.lateral_derecho)
        self.entrada.place(x=50, y=40)
        self.nombre.place(x=10, y=40)
        self.telefono = tk.Label(self.lateral_derecho, text="Telefono", bg="white", font=("Roboto", 11,"bold"))
        self.ent_telefono = tk.Entry(self.lateral_derecho)
        self.ent_telefono.place(x=250, y=40)
        self.telefono.place(x=175, y=40)
        self.fecha = tk.Label(self.lateral_derecho, text="Fecha alta", bg="white", font=("Roboto", 11,"bold"))
        self.ent_fecha = tk.Entry(self.lateral_derecho)
        self.fecha.place(x=10, y=90)
        self.ent_fecha.place(x=90, y=90)
        self.tratamiento = tk.Label(self.lateral_derecho, text="Tratamiento", bg="white", font=("Roboto", 11,"bold"))
        self.ent_tratamiento = tk.Entry(self.lateral_derecho)
        self.tratamiento.place(x=190, y=90)
        self.ent_tratamiento.place(x=285, y=90)

        
        
        # Create buttons form_clientes
       
    

        

    def form_productos(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Productes", 
                                              font="Roboto", bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

        # buttons form_productos

    def form_casos(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Cassos", 
                                              font="Roboto", bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

        # buttons from_casos

    def form_buscar(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Cercar", 
                                              font="Roboto", bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

        # buttons form_buscar

    def insertar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self):
        pass

    def cancelar(self):
        pass

    

