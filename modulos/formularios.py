import tkinter as tk
from tkinter import ttk
#from appGestion.datos.conexion import Conexion


class Formularios(tk.Tk, object):

    def __init__(self, lateral_derecho, nom=None, cognom=None, email=None, tel=None, data=None, trac=None):

        super().__init__()
        self.nombre = nom
        self.cognom = cognom
        self.email = email
        self.tel = tel
        self.data = data
        self.trac = trac
        self.entrada = None
        self.bnuevo = False
        self.bguardar = False
        self.bcancelar = False
        self.lateral_derecho_label = False
        self.cercar = False
        self.listar = False
        self.listar_clients = False
        self.listar_cassos = False
        self.listar_productes = False
        self.lateral_derecho = lateral_derecho
        self.entradas = []

    def frames(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)

    def etiqueta(self, text):

        info_label = [text]
        for text in info_label:
            self.lateral_derecho_label = tk.Label(self.lateral_derecho, text=f"{text}",
                                                  font=("Roboto", 15, "bold"),
                                                  bg="white", fg="blue")
            self.lateral_derecho_label.pack(expand=tk.NO)

    def labels_entry(self, text, x, y):
        info_entry = [text]
        coordenadas = [(x, y)]
        for text in info_entry:
            self.nombre = tk.Label(self.lateral_derecho, text=f"{text}", bg="white",
                                   font=("Roboto", 11, "bold"))
        for x, y in coordenadas:
            self.nombre.place(x=f"{x}", y=f"{y}")

    def entrys(self, x, y, ancho):

        self.entradas = []
        coordenadas = [(x, y, ancho)]
        for idx, (x, y, ancho) in enumerate(coordenadas):
            var = tk.StringVar()
            entrada = tk.Entry(self.lateral_derecho, textvariable=var)
            entrada.place(x=f"{x}", y=f"{y}", height=f"{ancho}")
            self.entradas.append((f"{entrada}", f"{var}"))

    def botones_form(self, x, y):

        ancho_menu = 8
        alto_menu = 1
        coordenadas = [(x, y)]
        #conexion = Conexion()

        self.bnuevo = tk.Button(self.lateral_derecho, cursor="hand2")
        self.bguardar = tk.Button(self.lateral_derecho,cursor="hand2")
        self.bcancelar = tk.Button(self.lateral_derecho, cursor="hand2")

        boton_form = [("Nou", self.bnuevo),
                      ("Guardar", self.bguardar),
                      ("Cancel·lar", self.bcancelar)]
        color = ["sky blue", "green", "red"]
        for idx, (text, button) in enumerate(boton_form):
            self.config_boton(button, text, ancho_menu, alto_menu)

            color_indice = idx % len(color)
            button.config(text=f"{text}", bd=0, bg=f"{color[color_indice]}",
                          font="Roboto", fg="white",
                          width=ancho_menu, height=alto_menu)

        for idx, (x, y) in enumerate(coordenadas):
            self.bnuevo.place(x=f"{x}", y=f"{y}")
            x += 100
            self.bguardar.place(x=f"{x}", y=f"{y}")
            x += 100
            self.bcancelar.place(x=f"{x}", y=f"{y}")
        self.encima_fuera(self.bnuevo)
        self.dentro_fuera_bguardar(self.bguardar)
        self.dentro_fuera_bcancelar(self.bcancelar)

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

    def config_boton(self, button, text, ancho_menu, alto_menu):
        self.config_boton(button, text, ancho_menu, alto_menu)
