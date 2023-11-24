import tkinter as tk
from  tkinter.ttk import *
import sqlite3
from modulos.gestio import *

# from gestio import afegir, modificar, eliminar, cerca


# finestra login

# finestra principal
main = tk.Tk()
main.title('Gestió')
main.resizable(0,0)
main.geometry("1200x650+100+10")
icono = tk.PhotoImage(file="images/yii.png")
main.iconphoto(True, icono)

# Menú lateral
lateral_izquierdo = tk.Frame(main, relief=tk.SOLID, width=200, height=650, padx=10, pady=10, bg='sky blue')
lateral_izquierdo.pack(side="left", expand=tk.NO)

# botones
estilo = ttk.Style()
estilo.configure("Clientes.TButton", padding=0, foreground="DeepSkyBlue2", background="LightSkyBlue1", border="None")
insertar = ttk.Button(lateral_izquierdo, text="Clientes", style="Clientes.TButton")
insertar.place(x=10, y=150)

estilo = ttk.Style()
estilo.configure("Productos.TButton", padding=0, foreground="DeepSkyBlue2", background="LightSkyBlue1", border="None")
insertar = ttk.Button(lateral_izquierdo, text="Productos", style="Productos.TButton")
insertar.place(x=10, y=180)

estilo = ttk.Style()
estilo.configure("Casos.TButton", padding=0, foreground="DeepSkyBlue2", background="LightSkyBlue1", border="None")
insertar = ttk.Button(lateral_izquierdo, text="Casos", style="Casos.TButton")
insertar.place(x=10, y=210)

estilo = ttk.Style()
estilo.configure("Buscar.TButton", padding=0, foreground="DeepSkyBlue2", background="LightSkyBlue1", border="None")
insertar = ttk.Button(lateral_izquierdo, text="Buscar", style="Buscar.TButton")
insertar.place(x=10, y=240)

estilo = ttk.Style()
estilo.configure("Salir.TButton", padding=0, foreground="DeepSkyBlue2", background="LightSkyBlue1", border="None")
insertar = ttk.Button(lateral_izquierdo, text="Salir", style="Salir.TButton")
insertar.place(x=10, y=500)

# part dreta, contingut
lateral_derecho = tk.Frame(main, relief=tk.SOLID, bg="white")
lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)





main.mainloop()

if __name__ == "__main__":
    con = sqlite3.connect('baseDatos/gestion.db')
    
