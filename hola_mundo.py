'''
GUI = Grafical User Interface
Tkinter = TK Interface, se debe de importar el modulo de tkinter

Grid en tkinter funciona por medio de columnas y filas, con una numeracion es especifico
o,o     1.0     2.0
0,1     1.1     2.1
0,2     1,2     2,2
0,3     1,3     2,3

padding es el espacio que se deja entre los elementos y el margen de los elementos:
Dentro del componente: se aplica en el grid
ipadx = valor en pixeles a la derecha e izquierda
ipady = espacion entre la parte superior e inferior

Fuera del componente: se aplica en el grid
pady = izquierda y derecha
padx = superior e inferior

'''

import tkinter as tk
#importamos el modulo del tema tkinter que es donde estan los componentes
from tkinter import ttk

'''
#Peimer ejersicio
#Creamos un objeto/instancia utilizando la clase tk, para crear nuestra ventana
ventana = tk.Tk()
#modificamos el tamaño de la ventana en pixeles
ventana.geometry('600x400')
#Cambiamos el nombre de la ventana
ventana.title('Hola mundo ')
#Configuramos el icono de la aplicacion
ventana.iconbitmap('icono.ico')



#antes de crear el boton debemos de crear el evento o metodo a utilizar
def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecucion del evento click')
    #creamos un nuevo componente
    boton2 = ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()

#Creamos un boton conocido como componente o widget, al crear un componente debemos especificar quien sera el padre,
#de este objeto o donde se colocara este nuevo objeto, y debemos de importar ttk
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)
#utilizar el pack layout manager para mostrar el boton en la ventana
boton1.pack()



#Iniciamos la ventana(esta linea la ejecutamos al final)
#si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()#hace que muestre la ventana
'''


'''
para dejar un boton estatico es con la funcion sticky = pegajoso 
se queda fijo en un solo lugar

nw nort west        n nort      ne nort east 
w west                          e east
sw sourth west      s sout      se sourth east

                    ns tola la columna central
                    ws toda la fila central 

'''


#2. Ejemplo con tkinter
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')

#Configurar el grid
ventana.rowconfigure(0, weight=1)#1er renglon ocupa - espacio que el 2do
ventana.rowconfigure(1,weight=10)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=5)


#   Metodos de los eventos
def evento1():
    boton1.config(text='Boton 1 presionado')#config nos permite cambiar la configuracion del mismo despues de hacer el evento
def evento2():
    boton2.config(text='Boton 2 presionado')
def evento3():
    boton3.config(text='Boton 3 presionado')
def evento4(): #fg foreground primer plano permite cambiar el color de la fuente
    boton4.config(text='Boton 4 presionado',fg='blue',relief=tk.GROOVE,background='gray')#RELIEF modifica el relieve


#definimos 2 botones
boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
#boton1.pack()#con pack lo agregamos a nuestra ventana
#para combinar celdas con 'columnspan' y filas con 'rowspan'
boton1.grid(row=0, column=0,sticky='NSWE',padx=40,pady=40,
            ipadx= 20,ipady=10,columnspan=2,rowspan=2)

#n(arriba), e(derecha), r(abajo), w(izquierda)
#tambien se puede usar  tk.N,S,E etc en lugar de la cadena
boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
#boton2.grid(row=1,column=0, sticky='NSWE')#CON W EL boton se carga a la izq

boton3 = ttk.Button(ventana, text='Boton 3', command=evento3)
boton3.grid(row=0, column=3, sticky='NSWE')

#tk nos permite acceder a mas configuraciones de diseño y ttk no
boton4 = tk.Button(ventana, text='Boton 4', command=evento4)
#boton4.grid(row=1, column=1, sticky='NSWE')

ventana.mainloop()#mainloop recive todos los eventos y muestra la aventana



