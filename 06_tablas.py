'''
Tablas
'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='DarkOliveGreen4')
ventana.title('Creacion de Tabla')
ventana.iconbitmap('tabla.ico')

#configurar el grid, indica que tendra una columna con el peso de uno y centrara nuestra tabla
ventana.columnconfigure(0, weight=1)
#aGREGAR LA COLUMNA para el scroll
ventana.columnconfigure(1, weight=0)

#Definir un estilo
estilos = ttk.Style()
estilos.theme_use('clam') #prepara el manejo del tema obscuro
estilos.configure('Treeview', background='DarkOliveGreen3',
                 foreground='white',
                 filedbackground='DarkOliveGreen4',
                 rowheight=30)
estilos.map('Treeview', background=[('selected', 'DarkOliveGreen4')])

#definir las columas, vista de arbol, crea 4 columnas y la primera muestra mas detalle referente a subregistros
#la podemos eliminar o omitir con show(geadings
columnas = ('Id','Nombre','Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')
tabla.grid(row=0, column=0)


#Agregar los cabeceros ala tabla, ANCHOR = anclar o ancla para centrar o mover el encabezado a la izq o der
tabla.heading('Id', text='Id',anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre',anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)


#agregar la inf que tendra la tabla, tambien podemos dar formato
tabla.column('Id', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)


#cARGAR LOS DAtos a la tabla a traves de una tupla
datos = ((1,'Giovanni',31),(2,'Angelica',39),(3,'Raquel',54)) + ((1,'Giovanni',31),(2,'Angelica',39),(3,'Raquel',54)) + ((1,'Giovanni',31),(2,'Angelica',39),(3,'Raquel',54)) + ((1,'Giovanni',31),(2,'Angelica',39),(3,'Raquel',54))
#iteramos la tupla para insertar la informacion en la tabla
for persona in datos:
    #parent='' lo dejamos vacio ya que no tendremos subregistros, index=END indica que cada registro se agregar al final uno tras otro
    #values = persona que es nuestra tupla
    tabla.insert(parent='',index=tk.END, values=persona)

#agregamos el scroll bar
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

#mostrar registro seleccionado
def mostrar_registro_seleccionado(event):
    print('Ejecutando metodo mostrar registro seleccionado')
    elemento_seleccionado = tabla.selection()[0]#solo procesamos el 1er registro
    elemento= tabla.item(elemento_seleccionado)#item
    persona = elemento['values']#Tupla de persona
    showinfo('Datos seleccionados', f'Persona: {persona}')
    print(persona)

#asociamos el evento select a la tabla
tabla.bind('<<TreeviewSelect>>', mostrar_registro_seleccionado)

#Publicamos la tabla
tabla.grid(row=0, column=0, sticky=tk.NSEW)

if __name__ == '__main__':
    ventana.mainloop()
