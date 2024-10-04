'''
Componentes entry

'''
import  tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')

#ttk.entry crea una ventana para entrada de datos
#width es la cantidad de caracteres que ocupa la caja
#show = nos permite capturar inf sin que sea visible asignando un caractes en especifico como este *
#entrada1 = ttk.Entry(ventana, width= 30, justify=tk.CENTER,show='*')
#entrada1 = ttk.Entry(ventana, width= 30, justify=tk.CENTER, state=tk.DISABLED) diseabled desabilita la caja de texto


#tk.DISABLED = desabilita la caja de texto, justify=tk.CENTER(Justifica el contenido)
#Definimos una variable que podremos modificar posteriormente (set), leer (get)
entrada_var1 = tk.StringVar(value='Valor por default')                   #Para asociar la variable a la caja de texto usamos "Textvariable + LA variable -> entrada_var1"
entrada1 = ttk.Entry(ventana, width= 30,textvariable=entrada_var1 )      #normal la habilita, se puede omitir ya que es su valor por defecto: state=tk.NORMAL
entrada1.grid(row=0, column=0)



#insert agrega un texto a la caja de texto
#entrada1.insert(0,'Introduce una cadena')
#entrada1.insert(5,'-')
#entrada1.insert(tk.END,'.')#tk.END = inserta inf al final de la cadena
#state='readonly deja el componente de entrada en solo lectura
#entrada1.config(state='readonly')

#asociar variables a la caja de texto para hacer cambios

def enviar():
    #1. Forma
    '''print(entrada1.get())
    boton1.config(text=entrada1.get())
    #Eliminar el contenido de la caja de texto, desde el incice 0 al final tk.END
    #entrada1.delete(0,tk.END)
    #seleccionar el texto de la caja
    entrada1.select_range(0,tk.END)
    #PARA HACER EFECTIVA LA SELECCION DEL TEXTO
    entrada1.focus()'''
    #2. Forma, recuperar la informacion a partir de una variable, asociada con la caja de texto
    boton1.config(text=entrada_var1.get())
    #Para una modificacion utilizamos la variable de texto y el metodo set, y no el componente
    entrada_var1.set('Cambio...')
    #recuperamos la informacion
    print(entrada_var1.get())

#Creamos un boton
boton1 = ttk.Button(text='Enviar', command=enviar)
boton1.grid(row=0,column=1)

ventana.mainloop()
