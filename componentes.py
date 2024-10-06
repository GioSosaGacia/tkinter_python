'''
Tabuladores
'''
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Componentes')
ventana.iconbitmap('icono.ico')

def crear_componentes_tabulador1(tabulador):
    #agregamos etiqueta y componente de entrada
    etiqueta1 = ttk.Label(tabulador, text='Nombre: ')
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)

    def enviar():
        messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')
    #Agregamos un boton
    boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)

def crear_componentes_tabulador2(tabulador):#Tabulador es donde se agregaran los componentes
    contenido = 'Este es mi texto con el contenido'
    #creamos el componente de scroll, importamos scrolledtext, wrap: tk.WORD justifica el texto
    # y muestra las palabras comletas cuando se llega al limite
    scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    #mostramos el componente
    scroll.grid(row=0, column=0)

def crear_componentes_tabulador3(tabulador):
    #crear una lista usando data list comprehensions, x+1 para que no inicie en 0 y comienze del 1
    #1.Expresion, 2.Ciclo for, 3.elemento a iterar
    datos = [x+1 for x in range(10)]
    #Creamos el objeto de tipo combobox
    combobox = ttk.Combobox(tabulador, width=15, values=datos)
    #Lo posicionamos o publicamos
    combobox.grid(row=0, column=0, padx=10, pady=10)
    #"Seleccionamos un elemento por defaul a mostrar"
    combobox.current(0)
    #Agregar un boton para saber que opcion selecciono el usuario
    def mostrar_valor():
        messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {combobox.get()}')
    boton1 = ttk.Button(tabulador, text='Mostrar valor seleccionado', command=mostrar_valor)
    boton1.grid(row=0, column=1)


def crear_tabs():
    #creamos un tab control con la clase Notebook
    control_tabulador = ttk.Notebook(ventana)
    #agregar un frame para agregar mas componentes dentro del tab y organizar los elementos
    tabulador1 = ttk.Frame(control_tabulador)
    #agregamos el tabulador al control de tabuladores:
    control_tabulador.add(tabulador1, text='Tabulador 1')
    #mostramos el tabulador
    control_tabulador.pack(fill='both')
    #creamos un metodo, componentes del tabulador 1
    crear_componentes_tabulador1(tabulador1)

    #creamos un tabulador 2
    tabulador2 = ttk.LabelFrame(control_tabulador,text='Contenido')#labelframe agrega un encabezado/titulo al tabulador 2
    control_tabulador.add(tabulador2, text='Tabulador 2')
    #creamos los componenetes del segundo tabulador
    crear_componentes_tabulador2(tabulador2)

    #creamos tabulador 3 , donde lo queremos colocar, en el control tabulador
    tabulador3 = ttk.LabelFrame(control_tabulador, text='DataList')
    #indicar donde vamos agregar el frame con el metodo add()
    control_tabulador.add(tabulador3, text='Tabulador 3')
    #creamos los componentes del 3re tabulador
    crear_componentes_tabulador3(tabulador3)

crear_tabs()
ventana.mainloop()
