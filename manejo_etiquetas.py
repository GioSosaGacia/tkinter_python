
'''
Manejo de etiquetas tkinter:


'''

import  tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')
ventana.iconbitmap('icono.ico')

entrada_var1 = tk.StringVar(value='Valor por default')                   #Para asociar la variable a la caja de texto usamos "Textvariable + LA variable -> entrada_var1"
entrada1 = ttk.Entry(ventana, width= 30,textvariable=entrada_var1 )      #normal la habilita, se puede omitir ya que es su valor por defecto: state=tk.NORMAL
entrada1.grid(row=0, column=0)

#etiqueta Label
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)# ubicacion


def enviar():
    #Modificamos el texto del label
    etiqueta1.config(text=entrada_var1.get())
    print(entrada_var1.get())

#Creamos un boton
boton1 = ttk.Button(text='Enviar', command=enviar)
boton1.grid(row=0,column=1)

ventana.mainloop()

