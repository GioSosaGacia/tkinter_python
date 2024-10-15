'''
Ventanas con POO
'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()#constructor de la clase padre de Tk
        #congigurar la ventana
        self.configurar_ventana()
        #configurar el grid
        self.configurar_grid()
        #Mostrar tabla
        self.mostrar_tabla()



    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(background='DarkOliveGreen4')
        self.title('Manejo de ventanas con POO')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)#mostrara la tabla
        self.columnconfigure(1, weight=0)#mostrara el scrollbar

    def mostrar_tabla(self):
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
        self.tabla = ttk.Treeview(self, columns=columnas, show='headings')


        #Agregar los cabeceros ala tabla, ANCHOR = anclar o ancla para centrar o mover el encabezado a la izq o der
        self.tabla.heading('Id', text='Id',anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre',anchor=tk.W)
        self.tabla.heading('Edad', text='Edad', anchor=tk.W)

        #agregar la inf que tendra la tabla, tambien podemos dar formato
        self.tabla.column('Id', width=80)
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Edad', width=120)

         #cARGAR LOS DAtos a la tabla a traves de una tupla
        datos = ((1,'Giovanni',31),(2,'Angelica',39),(3,'Raquel',54)) + ((1,'Giovanni',31),(2,'Angelica',39),(3,'Raquel',54)) + ((1,'Giovanni',31),(2,'Angelica',39),(3,'Raquel',54)) + ((1,'Giovanni',31),(2,'Angelica',39),(3,'Raquel',54))
        #iteramos la tupla para insertar la informacion en la tabla
        for persona in datos:
            #parent='' lo dejamos vacio ya que no tendremos subregistros, index=END indica que cada registro se agregar al final uno tras otro
            #values = persona que es nuestra tupla
            self.tabla.insert(parent='',index=tk.END, values=persona)

        #agregamos el scroll bar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        #asociamos el evento select a la tabla
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_registro_seleccionado)

        #Publicamos la tabla
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)

        #Publicamos la tabla
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)

    def mostrar_registro_seleccionado(self, event):
        print('Ejecutando metodo mostrar registro seleccionado')
        elemento_seleccionado = self.tabla.selection()[0]#solo procesamos el 1er registro
        elemento= self.tabla.item(elemento_seleccionado)#item
        persona = elemento['values']#Tupla de persona
        showinfo('Datos seleccionados', f'Persona: {persona}')
        print(persona)



if __name__ == '__main__':
    app = App()
    app.mainloop()
