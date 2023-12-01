import tkinter as tk
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

       ancho_menu = 20
       alto_menu = 2
        
       self.bclientes = tk.Button(self.lateral_izquierdo, command=self.clients)
       self.bproductos = tk.Button(self.lateral_izquierdo, command=self.productes)
       self.bcasos = tk.Button(self.lateral_izquierdo, command=self.cassos)
       self.bbuscar = tk.Button(self.lateral_izquierdo, command=self.buscar)
       self.bsortir =tk.Button(self.lateral_izquierdo, command=self.salida)

       info_boton = [("Clients", self.bclientes),
                     ("Productes",self.bproductos),
                     ("Cassos", self.bcasos),
                     ("Cercar", self.bbuscar),
                     ("Sortir", self.bsortir)]
       for text, button in info_boton:
            self.config_boton(button, text, ancho_menu, alto_menu)
        
    
    def config_boton(self, button, text, ancho_menu, alto_menu):
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

    
    def clients(self):

       if (self.bclientes['state'] == tk.NORMAL):
            self.bclientes['state'] = tk.DISABLED
            self.bcasos['state'] = tk.NORMAL
            self.bproductos['state'] = tk.NORMAL
            self.bbuscar['state'] = tk.NORMAL
            Formularios.form_clientes(self)
       else:
            self.bclientes['state'] = tk.NORMAL
        
        
    def productes(self):

        if (self.bproductos['state'] == tk.NORMAL):
            self.bclientes['state'] = tk.NORMAL
            self.bcasos['state'] = tk.NORMAL
            self.bproductos['state'] = tk.DISABLED
            self.bbuscar['state'] = tk.NORMAL

        if self.lateral_derecho is not None:
            self.lateral_derecho.pack_forget()
            Formularios.form_productos(self)

    def cassos(self):
        if (self.bcasos['state'] == tk.NORMAL):
            self.bclientes['state'] = tk.NORMAL
            self.bproductos['state'] = tk.NORMAL
            self.bcasos['state'] = tk.DISABLED
            self.bbuscar['state'] = tk.NORMAL
        
        if self.lateral_derecho is not None:
            self.lateral_derecho.pack_forget()
            Formularios.form_casos(self)

    def buscar(self):
        if (self.bbuscar['state'] == tk.NORMAL):
            self.bclientes['state'] = tk.NORMAL
            self.bproductos['state'] = tk.NORMAL
            self.bcasos['state'] = tk.NORMAL
            self.bbuscar['state'] = tk.DISABLED

        if self.lateral_derecho is not None:
            self.lateral_derecho.pack_forget()
            Formularios.form_buscar(self)

    def salida(self):
        exit()
    
