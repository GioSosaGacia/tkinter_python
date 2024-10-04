'''
    Manejo de mensajes tkinter
'''

import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')
ventana.iconbitmap('icono.ico')


entrada1 = ttk.Entry(ventana, width=30)                        #normal la habilita, se puede omitir ya que es su valor por defecto: state=tk.NORMAL
entrada1.grid(row=0, column=0)

#etiqueta Label
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)# ubicacion


def enviar():
    #Modificamos el texto del label
    etiqueta1.config(text=entrada1.get())
    #Messagebox o caja de mensajes
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + ' Informativo')
        messagebox.showerror('Mensaje Error', mensaje1 + ' Error')
        messagebox.showwarning('Mensaje informativo', mensaje1 + ' Warning')

#Creamos un boton
boton1 = ttk.Button(text='Enviar', command=enviar)
boton1.grid(row=0,column=1)

ventana.mainloop()
