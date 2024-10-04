'''
    Manejo de menus -> tkinter
'''
import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')
ventana.iconbitmap('icono.ico')


entrada1 = ttk.Entry(ventana, width=30)            #normal la habilita, se puede omitir ya que es su valor por defecto: state=tk.NORMAL
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

def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos de la aplicación!!')
    sys.exit()

def crear_menu():
    #configurar el menu principal
    menu_principal = Menu(ventana)
    #tearoff = false, hace que no se separe el menu de nuestra interfaz grafica
    submenu_archivo = Menu(menu_principal, tearoff=0)
    #Agregamos una nueva opcion al menu de archivo
    submenu_archivo.add_command(label='Nuevo')
    #agregar un separador
    submenu_archivo.add_separator()
    #agregamos la opcion de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    #agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')

    #submenu de ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    submenu_ayuda.add_command(label='Acerca De')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')

    #Mostramos el menu en la ventana principal
    ventana.config(menu=menu_principal)


#Creamos un boton
boton1 = ttk.Button(text='Enviar', command=enviar)
boton1.grid(row=0,column=1)

crear_menu()

ventana.mainloop()
