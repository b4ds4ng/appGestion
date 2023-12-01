import tkinter as tk



class Formularios(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        
    def form_clientes(self):

        # Create frame, label
        
   
        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Clients", 
                                              font="Roboto", bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.NO, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

        # Create entrys and labels

        self.nombre = tk.Label(self.lateral_derecho, text="Nom", bg="white")
        self.entrada = tk.Entry(self.lateral_derecho)
        self.entrada.place(x=45, y=40)
        self.nombre.place(x=10, y=40)

        # Create buttons
        
    

        

    def form_productos(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Productes", 
                                              font="Roboto", bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.NO, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

    def form_casos(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Cassos", 
                                              font="Roboto", bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.NO, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

    def form_buscar(self):

        self.lateral_derecho = tk.Frame(self, relief=tk.SOLID, bg="white")
        self.lateral_derecho_label = tk.Label(self.lateral_derecho, text="Formulario Cercar", 
                                              font="Roboto", bg="white", fg="blue")
        self.lateral_derecho.pack(side="right", expand=tk.NO, fill=tk.BOTH)
        self.lateral_derecho_label.pack(expand=tk.NO)

    def insertar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self):
        pass

    def cancelar(self):
        pass

    

