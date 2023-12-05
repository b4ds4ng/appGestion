import tkinter as tk
from  tkinter import ttk, font





class Formularios(tk.Tk):
    
    #def __init__(self):
        #super().__init__()
        
        
        
        
    def form_clientes(self):

        # Create frame, label
        
        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Clients", 
                                              font=("Roboto", 10, "bold"), bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

        # Create entrys and labels
       
        self.nombre = tk.Label(self.lateral_derecho, text="Nom", bg="white", font=("Roboto", 11,"bold"))
        self.entrada = tk.Entry(self.lateral_derecho)
        self.entrada.place(x=50, y=40)
        self.nombre.place(x=10, y=40)

        self.telefono = tk.Label(self.lateral_derecho, text="Cognom", bg="white", font=("Roboto", 11,"bold"))
        self.ent_telefono = tk.Entry(self.lateral_derecho)
        self.ent_telefono.place(x=250, y=40)
        self.telefono.place(x=175, y=40)

        self.fecha = tk.Label(self.lateral_derecho, text="Data alta", bg="white", font=("Roboto", 11,"bold"))
        self.ent_fecha = tk.Entry(self.lateral_derecho)
        self.fecha.place(x=10, y=90)
        self.ent_fecha.place(x=90, y=90)

        self.tratamiento = tk.Label(self.lateral_derecho, text="Tractament", bg="white", font=("Roboto", 11,"bold"))
        self.ent_tratamiento = tk.Entry(self.lateral_derecho)
        self.tratamiento.place(x=190, y=90)
        self.ent_tratamiento.place(x=285, y=90)

        
        
        # Create buttons form_clientes
  

        ancho_menu = 10
        alto_menu = 1
        self.bnuevo = tk.Button(self.lateral_derecho)
        self.bnuevo.config(text="Nou", bd=0, bg="#0739a4", font="Roboto", fg="white",
                           width=ancho_menu, height=alto_menu)
        self.bnuevo.pack_configure(side="left", anchor=tk.NE )
        self.bnuevo.pack(padx=10, pady=110)
        
        self.bguardar = tk.Button(self.lateral_derecho)
        self.bguardar.config(text="Guardar", bd=0, bg="#11a40a", font="Roboto", fg="white",
                             width=ancho_menu, height=alto_menu)
        self.bguardar.pack_configure(side="left", anchor=tk.NE)
        self.bguardar.pack(padx=80, pady=110)

        self.bguardar = tk.Button(self.lateral_derecho)
        self.bguardar.config(text="Cancel·lar", bd=0, bg="#d2210f", font="Roboto", fg="white",
                             width=ancho_menu, height=alto_menu)
        self.bguardar.pack_configure(side="left", anchor=tk.NW)
        self.bguardar.pack(padx=0, pady=110)
        
       
    

        

    def form_productos(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Productes", 
                                              font=("Roboto", 10, "bold"), bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

        # buttons form_productos

    def form_casos(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Cassos", 
                                              font=("Roboto", 10, "bold"), bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

        # buttons from_casos

    def form_buscar(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Cercar", 
                                              font=("Roboto", 10, "bold"), bg="white", fg="blue")
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

    

