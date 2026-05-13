import tkinter as tk
from tkinter import ttk
from .conexion import Conexion,Altas,Eliminar,Actualizar



class Formularios(tk.Tk):

    def __init__(self, lateral_derecho):

        super().__init__()

        #self.entrada = []
        self.lateral_derecho_label = False
        self.entradas = []
        self.cercar = False
        self.valores = None
        self.id_seleccionado = None
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
        """ Aquí es processen els entry que arriben des de principal, i s'envien les dades
        a alta client en conexion.py."""
        campos = len(self.entradas)
        if campos == 6:
            valores = [entrada.get() for entrada in self.entradas]
            Altas.alta_cliente(valores)
            Formularios.vaciar_campos(self)
            if hasattr(self, 'listar_clients') and self.listar_clients:
                Formularios.refrescar_treeview(self, self.listar_clients, "SELECT * FROM clients")

        if campos == 3:
            valores = [entrada.get() for entrada in self.entradas]
            Altas.alta_cliente(valores)
            Formularios.vaciar_campos(self)
            if hasattr(self, 'listar_productes') and self.listar_productes:
                Formularios.refrescar_treeview(self, self.listar_productes, "SELECT * FROM productes")

        if campos == 2:
            valores = [entrada.get() for entrada in self.entradas]
            Altas.alta_cliente(valores)
            Formularios.vaciar_campos(self)
            if hasattr(self, 'listar_cassos') and self.listar_cassos:
                Formularios.refrescar_treeview(self, self.listar_cassos, "SELECT * FROM casos")

    """Es buiden els camps al prémer el botó cancel·lar"""
    def vaciar_campos(self):

        for entrada in self.entradas:
            entrada.delete(0, tk.END)

    def cargar_datos_seleccionados(self, event):
        tree = event.widget
        seleccion = tree.selection()
        if seleccion:
            item = seleccion[0]
            valores = tree.item(item, "values")
            
            # Vaciamos los campos antes de llenarlos
            Formularios.vaciar_campos(self)
            
            # Adaptamos los valores según el treeview para ignorar columnas que no tienen Entry
            if tree == getattr(self, "listar_clients", None):
                # Guardamos el ID (índice 0) para actualizar o borrar luego
                self.id_seleccionado = valores[0]
                # Saltamos el ID (índice 0) para rellenar los Entry
                valores_formulario = valores[1:]
            elif tree == getattr(self, "listar_cassos", None):
                # Tomamos solo Categoria y Tractament
                valores_formulario = valores[:2]
            elif tree == getattr(self, "listar_productes", None):
                # Omitimos Categoria si no hay entry para ella (ajusta esto si hace falta)
                valores_formulario = valores[1:]
            else:
                valores_formulario = valores

            # Rellenamos los Entry correspondientes
            for i, entry in enumerate(self.entradas):
                if i < len(valores_formulario):
                    entry.insert(0, valores_formulario[i])

    def refrescar_treeview(self, tree, query):
        """Refresca los datos de un widget Treeview."""
        if tree is None or not tree.winfo_exists():
            return

        # Limpiar treeview
        for i in tree.get_children():
            tree.delete(i)

        # Cargar nuevos datos
        cnx = Conexion.conexion()
        cursor = cnx.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for fila in rows:
            tree.insert('', "end", values=fila)
        cursor.close()
        cnx.close()


    @staticmethod
    def eliminar_lista_entradas():

      pass

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

    """Després d'introduir les dades en qualsevol formulari, es llistaran tots els clients, productes o 
    casos en un treeview."""

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
        
        # Enlazar el evento de selección
        self.listar_clients.bind("<<TreeviewSelect>>", lambda event: Formularios.cargar_datos_seleccionados(self, event))

        Formularios.refrescar_treeview(self, self.listar_clients, "SELECT * FROM clients")

    def listado_cassos(self):

        columns = ("Id","Categoria", "Tractament", "Descripció")
        self.listar_cassos = ttk.Treeview(self.lateral_derecho,
                                          columns=columns, show="headings")
        for text in columns:
            self.listar_cassos.column(column=f"{text}", width=50)
        self.listar_cassos.heading("Id", text="Id")
        self.listar_cassos.heading("Categoria", text="Categoria")
        self.listar_cassos.heading("Tractament", text="Tractament")
        self.listar_cassos.heading("Descripció", text="Descripció")
        self.listar_cassos.place(x=2, y=200, width=989, height=400)
        
        # Enlazar el evento de selección
        self.listar_cassos.bind("<<TreeviewSelect>>", lambda event: Formularios.cargar_datos_seleccionados(self, event))

        Formularios.refrescar_treeview(self, self.listar_cassos, "SELECT * FROM casos")

    def listado_productes(self):

        columns = ("Id","Categoria", "Nom", "Us", "Descripció")
        self.listar_productes = ttk.Treeview(self.lateral_derecho, columns=columns,
                                             show="headings")
        for text in columns:
            self.listar_productes.column(column=f"{text}", width=50)
        self.listar_productes.heading("Id", text="Id")
        self.listar_productes.heading("Categoria", text="Categoria")
        self.listar_productes.heading("Nom", text="Nom")
        self.listar_productes.heading("Us", text="Us")
        self.listar_productes.heading("Descripció", text="Descripció")
        self.listar_productes.place(x=2, y=200, width=989, height=400)
        
        # Enlazar el evento de selección
        self.listar_productes.bind("<<TreeviewSelect>>", lambda event: Formularios.cargar_datos_seleccionados(self, event))

        Formularios.refrescar_treeview(self, self.listar_productes, "SELECT * FROM productes")

    def lista_busqueda(self):
        """Dins del treeview s'estableix tota la lògica d'interacció amb la IA, que es troba al
        mòdul consultesia.py"""
        self.lista_busqueda = ttk.Treeview(self.lateral_derecho, show="headings")
        self.lista_busqueda.place(x=2, y=30, width=989, height=615)

    def actualizar_entradas(self):
        """ Aquí es processen els entry que arriben des de principal, i s'envien les dades
        a actualitzar client, productes i cassos en conexion.py."""
        campos = len(self.entradas)
        if campos == 6:
            valores = [entrada.get() for entrada in self.entradas]
            if self.id_seleccionado:
                valores.append(self.id_seleccionado)
            Actualizar.actualizar_bds(valores)
            Formularios.vaciar_campos(self)
            if hasattr(self, 'listar_clients') and self.listar_clients:
                Formularios.refrescar_treeview(self, self.listar_clients, "SELECT * FROM clients")

        if campos == 3:
            valores = [entrada.get() for entrada in self.entradas]
            Actualizar.actualizar_bds(valores)
            Formularios.vaciar_campos(self)
            if hasattr(self, 'listar_productes') and self.listar_productes:
                Formularios.refrescar_treeview(self, self.listar_productes, "SELECT * FROM productes")

        if campos == 2:
            valores = [entrada.get() for entrada in self.entradas]
            Actualizar.actualizar_bds(valores)
            Formularios.vaciar_campos(self)
            if hasattr(self, 'listar_cassos') and self.listar_cassos:
                Formularios.refrescar_treeview(self, self.listar_cassos, "SELECT * FROM casos")

    def eliminar_entradas(self):
        """ Aquí es processen els entry que arriben des de principal, i s'envien les dades
        a eliminar client, productes i cassos en conexion.py."""
        campos = len(self.entradas)
        if campos == 6:
            valores = [entrada.get() for entrada in self.entradas]
            if self.id_seleccionado:
                valores.append(self.id_seleccionado)
            Eliminar.eliminar_bds(valores)
            Formularios.vaciar_campos(self)
            if hasattr(self, 'listar_clients') and self.listar_clients:
                Formularios.refrescar_treeview(self, self.listar_clients, "SELECT * FROM clients")

        if campos == 3:
            valores = [entrada.get() for entrada in self.entradas]
            Eliminar.eliminar_bds(valores)
            Formularios.vaciar_campos(self)
            if hasattr(self, 'listar_productes') and self.listar_productes:
                Formularios.refrescar_treeview(self, self.listar_productes, "SELECT * FROM productes")

        if campos == 2:
            valores = [entrada.get() for entrada in self.entradas]
            Eliminar.eliminar_bds(valores)
            Formularios.vaciar_campos(self)
            if hasattr(self, 'listar_cassos') and self.listar_cassos:
                Formularios.refrescar_treeview(self, self.listar_cassos, "SELECT * FROM casos")
