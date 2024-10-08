'''
Calculadora
para poder personalizar los botones es mejor utilizar la libreria de tk que la de ttk
un frame es un contenedor que sirve para alojar otros widgets
*el método packs en Tkinter es útil cuando necesitamos posicionar los widgets en bloques específicos para después
    ponerlos en la ventana principal
'''
import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()#mandamos a llamar el constructor de la clase padre Tk
        self.geometry('400x324+650+222')
        self.resizable(0,0)# para que no se pueda modificar el tamaño
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        #Atributos de la clase
        self.expresion = ''  #la utilizaremos para usar la funcion eval() permite evaluar un str considerendo los valores aritmeticos que encuentre
        #Caja de texto de tipo input
        self.entrada = None
        #StringVar lo utilizamos para obtener o actualizar el valor del input
        self.entrada_texto = tk.StringVar()
        #Creación de los componentes
        self._creacion_componentes()


        #metodos de clase
        #Para crear los componentes
    def _creacion_componentes(self):
        #Creamos el 1re frame para la caja de texto
        entrada_frame = tk.Frame(self, width='400', height=50, bg='grey')
        #publicamos el objeto con pack
        entrada_frame.pack(side=tk.TOP) #side tk.top hace que lo posiciones arriba(top)
        #Agregamos la caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'),textvariable=self.entrada_texto, width=30, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)

        #2do Frame para la parte inferior de la calculadora
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()

        #primer renglon(Limpiar, ) bd = border,
        #boton de limpiar
        boton_limpiar = tk.Button(botones_frame, text='Limpiar', width='42', height=3, bd=0, bg='#eee', cursor='hand2', command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        #boton de dividir, lambda es una funcion anonima que permite llamar al objeto de la funcion sin ejecutar la funcion
        boton_dividir = tk.Button(botones_frame, text='/', width=12, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._evento_click('/'))\
                                    .grid(row=0, column=3, padx=1, pady=1)
        #boton_dividir.grid(row=0, column=3, padx=1, pady=1)    con tk podemos dar estilo a los botones con una sola linea sin usar el grid aparte en otra lines

        #segunda linea
        boton_siete = tk.Button(botones_frame, text='7', width=14, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(7))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)
        boton_ocho = tk.Button(botones_frame, text='8', width=13, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(8))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)
        boton_nueve = tk.Button(botones_frame, text='9', width=13, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(9))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)
        boton_multiplicar = tk.Button(botones_frame, text='*', width=12, height=3, bd=0, bg='#eee',cursor='hand2', command=lambda: self._evento_click('*'))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)

        #tercera linea
        boton_cuatro = tk.Button(botones_frame, text='4', width=14, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(4))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)
        boton_cinco = tk.Button(botones_frame, text='5', width=13, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(5))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)
        boton_seis = tk.Button(botones_frame, text='6', width=13, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(6))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)
        boton_menos = tk.Button(botones_frame, text='-', width=12, height=3, bd=0, bg='#eee',cursor='hand2', command=lambda: self._evento_click('-'))
        boton_menos.grid(row=2, column=3, padx=1, pady=1)

        #cuarta linea
        boton_uno = tk.Button(botones_frame, text='1', width=14, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(1))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)
        boton_dos = tk.Button(botones_frame, text='2', width=13, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(2))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)
        boton_tres = tk.Button(botones_frame, text='3', width=13, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(3))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)
        boton_suma = tk.Button(botones_frame, text='+', width=12, height=3, bd=0, bg='#eee',cursor='hand2', command=lambda: self._evento_click('+'))
        boton_suma.grid(row=3, column=3, padx=1, pady=1)

        #quita linea
        boton_cero = tk.Button(botones_frame, text='0', width=28, height=3, bd=0, bg='white',cursor='hand2', command=lambda: self._evento_click(0))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        boton_punto = tk.Button(botones_frame, text='.', width=13, height=3, bd=0, bg='#eee',cursor='hand2', command=lambda: self._evento_click('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)
        boton_evaluar = tk.Button(botones_frame, text='=', width=12, height=3, bd=0, bg='#eee',cursor='hand2', command=self._evento_evaluar)
        boton_evaluar.grid(row=4, column=3, padx=1, pady=1)

    def _evento_evaluar(self):
        try:
            #si la expresion es diferente a cadena vacia no hace nada, si no hace la operacion
            if self.expresion:
                #lo convertimos a str ya que es lo que recive la calculadora
                #eval() evalua si un str contiene operadores aritmrticos y si los tiene hace las operacion
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
                #al hacer la operacion resetea el valor de la expresion ´para iniciar de nuevo
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''


    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        #Concatenamos el nuevo elemento presionado a la expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)





if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()


