'''
Zona Fit con GUI
'''
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from zona_fit_gui.ClienteDao import ClienteDAO
from zona_fit_gui.cliente import Cliente


class App(tk.Tk):
    #CREAMOS UNA CONSTANTE
    COLOR_VENTANA = '#1D2D44'

    def __init__(self):
        super().__init__()
        self.id_cliente =None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit APP')
        self.configure(background=App.COLOR_VENTANA)
        #aplicamos estilos
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')#preparamos los estilos para el modo obscuro
        self.estilos.configure(self, backgroung=App.COLOR_VENTANA,
                               foreground='black',
                               fieldbackground='lightgrey')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit(GYM)',
                             font=('Arial',20),
                             background=App.COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_formulario = ttk.Frame()
        #Nombre
        nombrel = ttk.Label(self.frame_formulario, text='Nombre:', background='#1D2D44', foreground='white')
        nombrel.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_formulario)
        self.nombre_t.grid(row=0, column=1)

        apellidol = ttk.Label(self.frame_formulario, text='Apellido:',background='#1D2D44', foreground='white')
        apellidol.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_formulario)
        self.apellido_t.grid(row=1, column=1)

        membresial = ttk.Label(self.frame_formulario, text='Membresía:',background='#1D2D44', foreground='white')
        membresial.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_formulario)
        self.membresia_t.grid(row=2, column=1)

        #publicar el Frame
        self.frame_formulario.grid(row=1,column=0)

    def cargar_tabla(self):
        #creamos un frama para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        #definimos los estilos dela tabla
        self.estilos.configure('Treeview', background='black',
                               foreground='red',
                               filedbackground='#1D2D44',
                               rowheight=20)
        #definimos las columnas usando una tupla
        columnas = ('Id','Nombre','Apellido','Membresia')
        #show=headings permite solo mostrar las columnas que estamos indicando ya que existe una fantasma que es la primera(la cual muestra gerarquia de subregistros)
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')

        #Agregamos los cabeceros/headings
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)#anchor da formato al posicionamiento del texto y por default es center
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)

        #Definir las columnas
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)

        #Cargar los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente._id,
                                      cliente._nombre,
                                      cliente._apellido,
                                      cliente._membresia))#hacemos el unpacking

        #Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        #asociar el evento select para recuperar los datos de registro seleccionado
        self.tabla.bind('<<TreeviewSelect>>',self.cargar_cliente)


        #Publicamos la tabla
        self.tabla.grid(row=0, column=0)

        #Publicamos el frame de la tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        self.estilos.configure('TFrame', background='#1D2D44')

        #crear botones
        #boton de agregar
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar', command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)

        #boton de eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar', command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)

        #Boton limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar', command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)

        #estilo a los botones
        self.estilos.configure("TButton", background='#005f73', foreground='white')
        #map configura el estilo de los botones al posicionarno sobre ellos, ejemplo cambio de color
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        #publicar frame botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        #validar los campos
        if(self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion',
                          message='El valor de la membresia "No" es numerico')
                self.membresia_t.delete(0, tk.END)#si no es numerico limpia el campo desde el indice 0 asta el final
                self.membresia_t.focus_set()#focus para que el usuario pueda llenar de nuevo el valor
        else:
            showerror(title='Atención', message='Debe de llenar el formulario')
            self.nombre_t.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False

    def eliminar_cliente(self):
        pass

    def recargar_datos(self):
        #volver a cargar los datos de la tabla
        self.cargar_tabla()
        #limpiar los daros
        self.limpiar_datos()

    def guardar_cliente(self):
        #recuperar los valores de las cajas de texto de cada uno de los campos
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        ClienteDAO.insertar(cliente)
        showinfo(title='Agregar', message='Cliente agregado')
        #volvemos a mostrar lso datos y limpiamos el formulario
        self.recargar_datos()

#agregamos event para asociar el evento creado al dar click en un registro
    def cargar_cliente(self,event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values']#obtiene la tupla de valores del elemento selecionado
        #recuperar cada valor del cliente para llenar el formulario
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        #antes de cargar, limpiamos el formularios
        self.limpiar_formulario()
        #cargar los valores al formulario
        self.nombre_t.insert(0,nombre)
        self.apellido_t.insert(0,apellido)
        self.membresia_t.insert(0,membresia)


    def limpiar_datos(self):
        self.limpiar_formulario()
        #limpiar el id despues de cada seleccion
        self.id_cliente = None

    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)


if __name__ == '__main__':
    app = App()
    app.mainloop()
