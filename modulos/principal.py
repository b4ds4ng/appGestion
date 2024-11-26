import tkinter as tk
from tkinter import ttk
import sqlite3
from .formularios import Formularios



class Iniciador(tk.Tk):

    def __init__(self):
        super().__init__()
        self.ventana_principal()
        self.paneles()
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

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)

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
                     ("Cercar", self.bbuscar),
                     ("Sortir", self.bsortir)]

       for text, button in info_boton:
            self.config_boton(button, text, ancho_boton, alto_boton)
        
    
    def config_boton(self, button, text, ancho_boton, alto_boton):
        button.config(text=f"{text}", bd=0, bg="sky blue", font="Roboto", fg="white",
                      width=ancho_menu, height=alto_menu)
        button.pack()
        self.encima_fuera(button)

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
            Formularios.frames(self)
            Formularios.etiqueta(self, text="Clients")
            Formularios.labels_entry(self, text="Nom", x=10, y=50)
            Formularios.labels_entry(self, text="Cognom", x=180, y=50)
            Formularios.labels_entry(self, text="Email", x=390, y=50)
            Formularios.labels_entry(self, text="Tel", x=10, y=80)
            Formularios.labels_entry(self, text="Data alta", x=200, y=80)
            Formularios.labels_entry(self, text="Tractament", x=400, y=80)
            Formularios.entrys(self, x=50, y=50, ancho=20)
            Formularios.entrys(self, x=250, y=50, ancho=20)
            Formularios.entrys(self, x=440, y=50, ancho=20)
            Formularios.entrys(self, x=50, y=80, ancho=20)
            Formularios.entrys(self, x=270, y=80, ancho=20)
            Formularios.entrys(self, x=490, y=80, ancho=20)
            Formularios.botones_form(self, x=10, y=130)
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
            Formularios.frames(self)
            Formularios.etiqueta(self, text="Productes")
            Formularios.labels_entry(self, text="Categoria", x=10, y=50)
            Formularios.labels_entry(self, text="Nom", x=230, y=50)
            Formularios.labels_entry(self, text="Us", x=400, y=50)
            Formularios.labels_entry(self, text="Descripció", x=570, y=50)
            Formularios.entrys(self, x=90, y=50, ancho=20)
            Formularios.entrys(self, x=270, y=50, ancho=20)
            Formularios.entrys(self, x=430, y=50, ancho=20)
            Formularios.entrys(self, x=660, y=50, ancho=100)
            Formularios.botones_form(self, x=10, y=130)
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
            Formularios.frames(self)
            Formularios.etiqueta(self, text="Cassos")
            Formularios.labels_entry(self, text="Categoria", x=10, y=50)
            Formularios.labels_entry(self, text="Tractament", x=230, y=50)
            Formularios.labels_entry(self, text="Descripció", x=460, y=50)
            Formularios.entrys(self, x=100, y=50, ancho=20)
            Formularios.entrys(self, x=320, y=50, ancho=20)
            Formularios.entrys(self, x=550, y=50, ancho=120)
            Formularios.botones_form(self, x=10, y=130)
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
            Formularios.frames(self)
            Formularios.etiqueta(self, text="Cercar")
            Formularios.labels_entry(self, text="Nom", x=10, y=50)
            Formularios.entrys(self, x=50, y=50, ancho=20)
            Formularios.botones_buscar(self)

    def salida(self):
        exit()
    
