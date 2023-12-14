import tkinter as tk
from  tkinter import ttk, font



class Formularios(tk.Tk):
            
    def frames(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)

    def etiqueta(self, text):
        info_label = [(text)]
            
        for text in info_label:
            self.lateral_derecho_label = tk.Label(self.lateral_derecho, text=f"{text}",
                                                  font=("Roboto", 15, "bold"), bg="white", fg="blue")
            self.lateral_derecho_label.pack(expand=tk.NO)

    def labels_entry(self, text, x, y):
        info_entry = [(text)]
        coordenadas = [(x, y)]
        for text in info_entry:
            self.nombre = tk.Label(self.lateral_derecho, text=f"{text}", bg="white", 
                                   font=("Roboto", 11,"bold"))
        for x, y in coordenadas:
            self.nombre.place(x=f"{x}", y=f"{y}")

    def entrys(self, x, y):
        coordenates =[(x, y)]
        for x, y in coordenates:
            self.entrada = tk.Entry(self.lateral_derecho)
            self.entrada.place(x=f"{x}", y=f"{y}")
    
    def botones_form(self, x, y):
        ancho_menu = 8
        alto_menu = 1
        coordenadas = [(x, y)]  
               
        self.bnuevo = tk.Button(self.lateral_derecho, cursor="hand2")
        self.bguardar = tk.Button(self.lateral_derecho, cursor="hand2")
        self.bcancelar = tk.Button(self.lateral_derecho, cursor="hand2")

        boton_form = [("Nou", self.bnuevo),
                      ("Guardar", self.bguardar),
                      ("Cancel·lar", self.bcancelar)]
        
        for text, button in boton_form:
            self.config_boton(button, text, ancho_menu, alto_menu) 
    
            for x, y in coordenadas:
                self.bnuevo.place(x=f"{x}", y=f"{y}")
                x += 100
                self.bguardar.place(x=f"{x}", y=f"{y}")
                x += 100
                self.bcancelar.place(x=f"{x}", y=f"{y}")
             
            color = [("sky blue"), ("red"), ("green")]
            for i in color:
                
                button.config(text=f"{text}", bd=0, bg=f"{i}", font="Roboto", fg="white",
                                   width=ancho_menu, height=alto_menu)
                
                #self.bguardar.config(text=f"{text}", bd=0, bg=f"{i}", font="Roboto", fg="white",
                                     #width=ancho_menu, height=alto_menu)
                
                #self.bcancelar.config(text=f"{text}", bd=0, bg=f"{i}", font="Roboto", fg="white",
                                      #width=ancho_menu, height=alto_menu)
                
                 

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

    def listado(self):

        columns = ("Nom", "Cognom", "telefon", "Email")
        self.listar = ttk.Treeview(self.lateral_derecho, columns=columns, show="headings")
        self.listar.heading("Nom", text="Nom")
        self.listar.heading("Cognom", text="Cognom")
        self.listar.heading("telefon", text="Telèfon")
        self.listar.heading("Email", text="Email")
        self.listar.place(x=2, y=200)



       
        

