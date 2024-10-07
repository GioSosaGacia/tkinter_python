'''
Componentes con OPP
Cuando son metodos de clase todos deben de llevar el parametro self
'''
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

#herada de la clase tk
class Componentes(tk.Tk):

    def __init__(self):# en vez de la ventana utilizamos el parametro self, ya que heredamos las caracteristicas de la clase tk
        super().__init__()# hacemos la herencia de la clase Tk y su metodo __init__
        #Ventana Principal
        self.geometry('650x400+450+225')#los ultimos dos datos son para las cordenadas de donde de mostrara la ventana
        self.title('Componentes')
        self.iconbitmap('icono.ico')
        #Para que no permita hacer cambios en la ventama principal en cuestiones de tamaño
        #con resizable
        #self.resizable(0,0)#ejej x y eke y

        #configuracion del grid
        #self.columnconfigure(0, weight=1) #La primera columna mantendra un ancho de 1
        #self.columnconfigure(1,weight=3)#segunda columna con un ancho de 3
        self._crear_tabs()



    def _crear_componentes_tabulador1(self,tabulador):
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

    def _crear_componentes_tabulador2(self,tabulador):#Tabulador es donde se agregaran los componentes
        contenido = 'Este es mi texto con el contenido'
        #creamos el componente de scroll, importamos scrolledtext, wrap: tk.WORD justifica el texto
        # y muestra las palabras comletas cuando se llega al limite
        scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        #mostramos el componente
        scroll.grid(row=0, column=0)

    def _crear_componentes_tabulador3(self,tabulador):
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

    def _crear_componentes_tabulador4(self,tabulador):
        imagen = tk.PhotoImage(file='python-logo.png')
        def mostrar_titulo():
            messagebox.showinfo('Mas informacion de la imagen', f'Nombre de la Imagen: {imagen.cget("file")}')#cget recupera el nombre del archivo de la imagen
        boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
        boton_imagen.grid(row=0, column=0)

    def _crear_componentes_tabulador5(self, tabulador):
        #creamos el componente de barra de progreso al subir un archivo
        barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
        barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        #Metodos para comtrolar los eventos de la barra de progreso
        def ejecutar_barra():
            #indica el maximo de la barra de progreso
            barra_progreso['maximum'] = 100
            for valor in range(101):
                #mandamos a esperar un poco antes de continuar con la ejecucion de la barra
                sleep(0.05)#lo importamos de la libreria de time
                #incrementamos la barra de progreso
                barra_progreso['value'] = valor
                #para que se refleje actualizamos nuestra barra de progreso
                barra_progreso.update()
                #Una vez que se ejecuto retornamos el valor a 0
            barra_progreso['value'] = 0
        def ejecutar_ciclo():
            barra_progreso.start()
        def detener():
            barra_progreso.stop()
        def detener_despues():
            esparar_ms = 2000
            self.after(esparar_ms, barra_progreso.stop)#after detiene la ejecusion de un componente despues de ciertos segundos
        #botones para controlar eventos de una barra de progreso
        boton_inicio = tk.Button(tabulador, text='Ejecutar barra de progreso', command=ejecutar_barra)
        boton_inicio.grid(row=1, column=0)
        boton_ciclo = tk.Button(tabulador, text='Ejecutar ciclo', command=ejecutar_ciclo)
        boton_ciclo.grid(row=1, column=1)
        boton_detener = ttk.Button(tabulador, text='Detener Ejecucion', command=detener)
        boton_detener.grid(row=1, column=2)
        boton_despues = ttk.Button(tabulador, text='Detener ejecucion despues de 2s', command=detener_despues)
        boton_despues.grid(row=1, column=3)


    def _crear_tabs(self):
        #creamos un tab control con la clase Notebook
        control_tabulador = ttk.Notebook(self)
        #agregar un frame para agregar mas componentes dentro del tab y organizar los elementos
        tabulador1 = ttk.Frame(control_tabulador)
        #agregamos el tabulador al control de tabuladores:
        control_tabulador.add(tabulador1, text='Tabulador 1')
        #mostramos el tabulador
        control_tabulador.pack(fill='both')
        #creamos un metodo, componentes del tabulador 1
        self._crear_componentes_tabulador1(tabulador1)

        #creamos un tabulador 2
        tabulador2 = ttk.LabelFrame(control_tabulador,text='Contenido')#labelframe agrega un encabezado/titulo al tabulador 2
        control_tabulador.add(tabulador2, text='Tabulador 2')
        #creamos los componenetes del segundo tabulador
        self._crear_componentes_tabulador2(tabulador2)

        #creamos tabulador 3 , donde lo queremos colocar, en el control tabulador
        tabulador3 = ttk.LabelFrame(control_tabulador, text='DataList')
        #indicar donde vamos agregar el frame con el metodo add()
        control_tabulador.add(tabulador3, text='Tabulador 3')
        #creamos los componentes del 3re tabulador
        self._crear_componentes_tabulador3(tabulador3)

        #creamos el tabulador 4
        tabulador4 = ttk.LabelFrame(control_tabulador, text='Imagen')
        control_tabulador.add(tabulador4, text='Tabulador 4')
        #creamos los componentes del tabuladpor 4
        self._crear_componentes_tabulador4(tabulador4)

        #creamos el tabulador 5
        tabulador5 = tk.LabelFrame(control_tabulador, text='Barra de progreso')
        control_tabulador.add(tabulador5, text='Tabulador 5')
        #creamos componentes del 5 tabulador
        self._crear_componentes_tabulador5(tabulador5)

#este metodo es parte de nuestra clase asi que se agrega al metodo init
#crear_tabs()



if __name__ == '__main__':
    #creamos un objeto de la clase
    componentes = Componentes()
    componentes.mainloop()
    #componentes2 = Componentes()
    #componentes2.mainloop()
