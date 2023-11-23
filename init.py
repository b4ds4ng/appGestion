import tkinter as tk
from  tkinter import ttk

# Ventana principal
main = tk.Tk()
main.title('Olga')
main.resizable(0,0)
main.geometry("1200x650+100+10")


# Menú lateral
lateral_izquierdo = tk.Frame(main, relief=tk.SOLID, width=200, height=650, padx=10, pady=10, bg='sky blue')
lateral_izquierdo.pack(side="left", expand=tk.NO)

# parte derecha
lateral_derecho = tk.Frame(main, relief=tk.SOLID, bg="white")
lateral_derecho.pack(side="right", expand=tk.YES, fill=tk.BOTH)





main.mainloop()

