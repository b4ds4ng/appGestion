import tkinter as tk
from  tkinter import ttk, Frame
import sqlite3



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
        #self.marc_clients = tk.Frame(self)
                                  
        #self.marc_clients.pack(side='right', expand=tk.YES, fill=tk.BOTH)
        
        self.lateral_izquierdo = tk.Frame(self, 
                                          relief=tk.SOLID, 
                                          width=200,   
                                          height=650, 
                                          padx=10, 
                                          pady=10, 
                                          bg='sky blue')
        self.lateral_izquierdo.pack(side="left", expand=tk.NO)

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)

    def botones(self):
        estilo = ttk.Style()
        estilo.configure("Clientes.TButton", 
                         padding=0, 
                         foreground="DeepSkyBlue2", 
                         background="LightSkyBlue1", 
                         border="None")

        clientes = ttk.Button(self.lateral_izquierdo, 
                              text="Clients", style="Clientes.TButton")
                              
        clientes.place(x=10, y=150)

        estilo = ttk.Style()
        estilo.configure("Productos.TButton", 
                         padding=0, 
                         foreground="DeepSkyBlue2", 
                         background="LightSkyBlue1", 
                         border="None")

        productos = ttk.Button(self.lateral_izquierdo, 
                               text="Productes", 
                               style="Productos.TButton")
        productos.place(x=10, y=180)

        estilo = ttk.Style()
        estilo.configure("Casos.TButton", 
                         padding=0, 
                         foreground="DeepSkyBlue2", 
                         background="LightSkyBlue1", 
                         border="None")
        casos = ttk.Button(self.lateral_izquierdo, 
                           text="Cassos", 
                           style="Casos.TButton")
        casos.place(x=10, y=210)

        estilo = ttk.Style()
        estilo.configure("Buscar.TButton", 
                         padding=0, 
                         foreground="DeepSkyBlue2", 
                         background="LightSkyBlue1", 
                         border="None")
        buscar = ttk.Button(self.lateral_izquierdo, 
                            text="Cercar", 
                            style="Buscar.TButton")
        buscar.place(x=10, y=240)

        estilo = ttk.Style()
        estilo.configure("Salir.TButton", 
                         padding=0, 
                         foreground="DeepSkyBlue2", 
                         background="LightSkyBlue1", 
                         border="None")
        salir = ttk.Button(self.lateral_izquierdo, 
                           text="Sortir", 
                           style="Salir.TButton")
        salir.place(x=10, y=500)