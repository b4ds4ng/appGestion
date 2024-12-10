import tkinter as tk
from tkinter import ttk
from .conexion import Altas





class Formularios(tk.Tk):



    def __init__(self, lateral_derecho):

        super().__init__()

        #self.entrada = []
        self.lateral_derecho_label = False
        self.entradas = []
        self.cercar = False
        self.listar_clients = False
        self.listar_cassos = False
        self.listar_productes = False
        self.lista_busqueda = False
        self.lateral_derecho = lateral_derecho





    def lateral_derecho(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)

    def etiqueta(self, text):

        info_label = [text]
        for text in info_label:
            self.lateral_derecho_label = tk.Label(self.lateral_derecho, text=f"{text}",
                                                  font=("Roboto", 15, "bold"),
                                                  bg="white", fg="sky blue")
            self.lateral_derecho_label.pack(expand=tk.NO)

    def leer_entradas(self):
        # Aquí es processen els entry que arriben des de principal.
        valores = []
        for entrada in self.entradas:
            valor = entrada.get()
            valores.append(valor)
        Altas.alta_cliente(valores)

    @staticmethod
    def prova_boton():
        print("botó cancel·lar premut" )

        # Aquí ficar la funció que neteja dels formularis. Reanomenar la funció.

    def botones_buscar(self):

        ancho_menu = 10
        alto_menu = 1
        self.cercar = tk.Button(self.lateral_derecho)
        self.cercar.config(text="Cercar", bd=0, bg="sky blue", font="Roboto", fg="white",
                           width=ancho_menu, height=alto_menu, state=tk.NORMAL,
                           cursor="hand2")
        self.cercar.pack_configure(side="left", anchor=tk.NE)
        self.cercar.pack(padx=10, pady=110)
        self.encima_fuera(self.cercar)

    def listado_clients(self):

        columns = (["Id", "Nom", "Cognom", "Email",
                    "Telèfon", "Us", "Tractament"])
        self.listar_clients = ttk.Treeview(self.lateral_derecho, columns=columns,
                                           show="headings")
        for text in columns:
            self.listar_clients.column(column=f"{text}", width=50)
        self.listar_clients.heading("Id", text="Id")
        self.listar_clients.heading("Nom", text="Nom") 
        self.listar_clients.heading("Cognom", text="Cognom")
        self.listar_clients.heading("Email", text="Email")
        self.listar_clients.heading("Telèfon", text="Telèfon")
        self.listar_clients.heading("Us", text="Us")
        self.listar_clients.heading("Tractament", text="Tractament")
        self.listar_clients.place(x=2, y=200, width=989, height=400)

    def listado_cassos(self):

        columns = ("Categoria", "Tractament", "Descripció")
        self.listar_cassos = ttk.Treeview(self.lateral_derecho,
                                          columns=columns, show="headings")
        for text in columns:
            self.listar_cassos.column(column=f"{text}", width=50)
        self.listar_cassos.heading("Categoria", text="Categoria")
        self.listar_cassos.heading("Tractament", text="Tractament")
        self.listar_cassos.heading("Descripció", text="Descripció")
        self.listar_cassos.place(x=2, y=200, width=989, height=400)

    def listado_productes(self):

        columns = ("Categoria", "Nom", "Us", "Descripció")
        self.listar_productes = ttk.Treeview(self.lateral_derecho, columns=columns,
                                             show="headings")
        for text in columns:
            self.listar_productes.column(column=f"{text}", width=50)
        self.listar_productes.heading("Categoria", text="Categoria")
        self.listar_productes.heading("Nom", text="Nom")
        self.listar_productes.heading("Us", text="Us")
        self.listar_productes.heading("Descripció", text="Descripció")
        self.listar_productes.place(x=2, y=200, width=989, height=400)


    def lista_busqueda(self):
        """Dins del treeview col·locar tota la lògica d'interacció amb la IA"""
        self.lista_busqueda = ttk.Treeview(self.lateral_derecho, show="headings")
        self.lista_busqueda.place(x=2, y=30, width=989, height=615)

