import tkinter as tk
from tkinter import ttk
import sqlite3
from .formularios import Formularios
from appGestion.datos.conexion import Conexion


class Iniciador(tk.Tk, object):

    def __init__(self):
        super().__init__()
        self.ventana_principal()
        self.paneles()
        self.lateral_derecho()
        self.entradas = []
        self.lateral_derecho_label = None
        self.botones()



    def ventana_principal(self):
        self.title('Gestió')
        self.resizable(0,0)
        self.geometry("1200x650+100+10")
        self.icono = tk.PhotoImage(file="./images/yii.png")
        self.iconphoto(True, self.icono)

    def paneles(self):
        
        self.lateral_izquierdo = tk.Frame(self, 
                                          relief=tk.SOLID, 
                                          width=200,   
                                          height=650, 
                                          padx=10, 
                                          pady=10, 
                                          bg='sky blue')
        self.lateral_izquierdo.pack(side="left", expand=tk.NO, fill=tk.BOTH)

    def lateral_derecho(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)

    def labels_entry(self, text, x, y):
        info_entry = [text]
        coordenadas = [(x, y)]
        for text in info_entry:
            nombre = tk.Label(self.lateral_derecho, text=f"{text}", bg="white",
                                   font=("Roboto", 11, "bold"))
        for x, y in coordenadas:
            nombre.place(x=f"{x}", y=f"{y}")


    def entrys(self, x, y, ancho):

        coordenadas = [(x, y, ancho)]

        for idx, (x, y, ancho) in enumerate(coordenadas):
            entrada = tk.Entry(self.lateral_derecho)
            entrada.place(x=f"{x}", y=f"{y}", height=f"{ancho}")
            self.entradas.append(entrada)

    def botones(self):

       ancho_boton = 20
       alto_boton = 2
        
       self.bclientes = tk.Button(self.lateral_izquierdo, command=self.clients, cursor="hand2")
       self.bproductos = tk.Button(self.lateral_izquierdo, command=self.productes, cursor="hand2")
       self.bcasos = tk.Button(self.lateral_izquierdo, command=self.cassos, cursor="hand2")
       self.bbuscar = tk.Button(self.lateral_izquierdo, command=self.buscar, cursor="hand2")
       self.bsortir = tk.Button(self.lateral_izquierdo, command=self.salida, cursor="hand2")

       info_boton = [("Clients", self.bclientes),
                     ("Productes",self.bproductos),
                     ("Cassos", self.bcasos),
                     ("Consultes", self.bbuscar),
                     ("Sortir", self.bsortir)]

       for text, button in info_boton:
            self.config_boton(button, text, ancho_boton, alto_boton)

    def config_boton(self, button, text, ancho_boton, alto_boton):
        button.config(text=f"{text}", bd=0, bg="sky blue", font="Roboto", fg="white",
                      width=ancho_boton, height=alto_boton)
        button.pack()
        self.encima_fuera(button)

    def botones_form(self):

        ancho_menu = 8
        alto_menu = 1
        x = 100
        y = 130
        coordenadas = [(x, y)]

        self.bnuevo = tk.Button(self.lateral_derecho,
                                  cursor="hand2")
        self.bguardar = tk.Button(self.lateral_derecho, command=lambda: Formularios.leer_entradas(self),
                                  cursor="hand2")
        self.bcancelar = tk.Button(self.lateral_derecho, command=lambda: Formularios.prova_boton(),
                                  cursor="hand2")
        boton_form = [("Nou", self.bnuevo),
                      ("Guardar", self.bguardar),
                      ("Cancel·lar", self.bcancelar)]
        color = ["sky blue", "green", "red"]
        for idx, (text, button) in enumerate(boton_form):

            self.configurar_boton(button, text, ancho_menu, alto_menu)
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

    def configurar_boton(self, button, text, ancho_menu, alto_menu):
        pass

    def encima_fuera(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg="sky blue", fg="#5ca7f2")

    def on_leave(self, event, button):
        button.config(bg="sky blue", fg="white")

    def dentro_fuera_bguardar(self, button):
        button.bind("<Enter>", lambda event: self.on_dentro(event, button))
        button.bind("<Leave>", lambda event: self.on_fuera(event, button))

    def on_dentro(self, event, button):
        button.config(bg="green3", fg="green4")

    def on_fuera(self, event, button):
        button.config(bg="green", fg="white")

    def dentro_fuera_bcancelar(self, button):
        button.bind("<Enter>", lambda event: self.on_dentro_bc(event, button))
        button.bind("<Leave>", lambda event: self.on_fuera_bc(event, button))

    def on_dentro_bc(self, event, button):
        button.config(bg="red3", fg="red4")

    def on_fuera_bc(self, event, button):
        button.config(bg="red", fg="white")

    def clients(self):

        if (self.bclientes['state'] == tk.NORMAL):
            self.bclientes['state'] = tk.DISABLED
            self.bcasos['state'] = tk.NORMAL
            self.bproductos['state'] = tk.NORMAL
            self.bbuscar['state'] = tk.NORMAL

        if self.lateral_derecho is None:
            self.lateral_derecho(self)

        else:
            self.lateral_derecho.pack_forget()
            Formularios.lateral_derecho(self)
            Formularios.etiqueta(self, text="Clients")
            self.labels_entry( "Nom", 10, 50)
            self.labels_entry("Cognom", 180, 50)
            self.labels_entry("Email", 390, 50)
            self.labels_entry("Tel", 10, 80)
            self.labels_entry("Data alta", 200, 80)
            self.labels_entry("Tractament", 400, 80)
            self.entrys(x=50, y=50, ancho=20)
            self.entrys(x=250, y=50, ancho=20)
            self.entrys(x=440, y=50, ancho=20)
            self.entrys(x=50, y=80, ancho=20)
            self.entrys(x=270, y=80, ancho=20)
            self.entrys(x=490, y=80, ancho=20)
            self.botones_form()
            Formularios.listado_clients(self)
        
    def productes(self):

        if (self.bproductos['state'] == tk.NORMAL):
            self.bclientes['state'] = tk.NORMAL
            self.bcasos['state'] = tk.NORMAL
            self.bproductos['state'] = tk.DISABLED
            self.bbuscar['state'] = tk.NORMAL

        if self.lateral_derecho is None:
            self.lateral_derecho(self)

        else:
            self.lateral_derecho.pack_forget()
            Formularios.lateral_derecho(self)
            Formularios.etiqueta(self, text="Categoria")
            self.labels_entry(text="Tractament", x=10, y=50)
            self.labels_entry(text="Us", x=230, y=50)
            self.labels_entry(text="Descripció", x=400, y=50)
            self.entrys(x=90, y=50, ancho=20)
            self.entrys(x=270, y=50, ancho=20)
            self.entrys(x=430, y=50, ancho=20)
            self.botones_form()
            Formularios.listado_productes(self)

    def cassos(self):
        if (self.bcasos['state'] == tk.NORMAL):
            self.bclientes['state'] = tk.NORMAL
            self.bproductos['state'] = tk.NORMAL
            self.bcasos['state'] = tk.DISABLED
            self.bbuscar['state'] = tk.NORMAL

            if self.lateral_derecho is None:
                self.lateral_derecho(self)

            else:

                self.lateral_derecho.pack_forget()
                Formularios.lateral_derecho(self)
                Formularios.etiqueta(self,text="Cassos")
                self.labels_entry(text="Categoria", x=10, y=50)
                self.labels_entry(text="Tractament", x=230, y=50)
                self.entrys(x=100, y=50, ancho=20)
                self.entrys(x=320, y=50, ancho=20)
                self.botones_form()
                Formularios.listado_cassos(self)

    def buscar(self):
        if (self.bbuscar['state'] == tk.NORMAL):
            self.bclientes['state'] = tk.NORMAL
            self.bproductos['state'] = tk.NORMAL
            self.bcasos['state'] = tk.NORMAL
            self.bbuscar['state'] = tk.DISABLED

            if self.lateral_derecho is None:
                self.lateral_derecho(self)

            else:

                self.lateral_derecho.pack_forget()
                Formularios.lateral_derecho(self)
                Formularios.etiqueta(self, text="Consultes")
                #self.labels_entry(text="Consulta", x=10, y=50)
                #self.entrys(x=80, y=50, ancho=20)
                #Formularios.botones_buscar(self)
                Formularios.lista_busqueda(self)

    def salida(self):
        exit()
    
