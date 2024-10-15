'''

    Editor de texto con tkinter
    FileDialog: permite abrir una ventana para seleccionar el archivo con el que deseamos trabajar
    permite guardar y abrir archivos

    Investigar como abrir archivos con formato pdf
'''
import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('giovanni-sosa-12@outlok.com Editor de texto')
        #configuracion de l tamaño minimo de la ventana
        self.rowconfigure(0, minsize=600, weight=1)
        #confiuracion minima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        #atributo de campo de texto
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        self.iconbitmap('note_102351.ico')
        #Atributo de archivo el cual tendra una referencia del mismo
        self.archivo = None
        #atributo para saber si ya tenemos un archivo abierto o no
        self.archivo_abierto = False
        self._crear_componentes()
        self._crear_menu()

    def _crear_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        boton_abrir = tk.Button(frame_botones, text='Abrir', command=self._abrir_archivo)
        boton_guardar = tk.Button(frame_botones,text='Guardar', command=self._guardar)
        boton_guardar_como = tk.Button(frame_botones, text='Guardar como...', command=self._guardar_como)
        #los botonoes los expandimos de manera horizonal: sticky = we de izquierda a derecha
        boton_abrir.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        boton_guardar_como.grid(row=2, column=0, sticky='we', padx=5, pady=5)
        #se coloca el frame de manera verticar de norte a sur ns
        frame_botones.grid(row=0, column=0, sticky='ns')
        #agregamos el campo de texto se expandira por completo el espacio disponible que le reste
        self.campo_texto.grid(row=0, column=1, sticky='nswe')

    def _crear_menu(self):
        #creamos el menu de la app
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)# el método self.configure(menu) sirve para editar las opciones de un menú:
        #agregamos las opciones al menu
        #Menu archivo
        menu_archivo = tk.Menu(menu_app, tearoff=False) #CON TEAROFF indicamos que la aplicacion no se puede separara del menu
        menu_app.add_cascade(label='Archivo', menu=menu_archivo)#crearun menu de tipo cascada
        #Agregamos las opciones del menu de archivo
        menu_archivo.add_command(label='Abrir', command=self._abrir_archivo)#add_command permite añadir items a un menu
        menu_archivo.add_command(label='Guardar', command=self._guardar)
        menu_archivo.add_command(label='Guardar como...', command=self._guardar_como)
        #agregar un separador
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir', command=self.quit)


    def _abrir_archivo(self):
        #Abrimos el archivo para edicion lectura escritura
        self.archivo_abierto = askopenfile(mode='r+')#askopenfile nos permitre abrir un archivo, modo r+ india que sera de r and w
        #eliminamos el texto anterior, previo al que se abrira
        self.campo_texto.delete(1.0, tk.END)
        #rEVISAMOS SI AHI UN ARCHIVO
        if not self.archivo_abierto:
            return
        #abrimos el archivo en modo lectura/escritura como un recurso
        with open(self.archivo_abierto.name, 'r+') as self.archivo:#name toma el nombre del recurso que se quiere abrir
            #leemos el contenido de larchivo
            texto = self.archivo.read()
            #Insertamos el contenido del archivo en el campo del texto
            self.campo_texto.insert(1.0, texto)
            #Modificamos el titulo de la aplicacion para saber cual archivo se abrio
            self.title(f'*Editor Texto - {self.archivo.name}') #El  * indica que modificaremos el archivo
    def _guardar(self):
        #Primero se reviza si un archivo ya fue abierto para sobree scribirlo
        if self.archivo_abierto:
            #Salvamos el archivo(Lo abrimos en modo escritura) para guardar la inf agregaga
            with open(self.archivo_abierto.name, 'w') as self.archivo:
                #leemos el contenido de la caja de texto
                texto = self.campo_texto.get(1.0, tk.END)
                #Escribimos el contenido al mismo archivo
                self.archivo.write((texto))
                #Cambiamos el nombre dle titulo de la app, quitamos el * para indicar que se guardo
                self.title(f'Editor Texto- {self.archivo.name}')
        else:
            self._guardar_como()
    def _guardar_como(self):
        #salvamos el archivo actual como un nuevo archivo
        self.archivo = asksaveasfilename(
            defaultextension='txt',             #'*.*' = muestra todos los archivos el primer * sin importar elnombre y el segundo .*= todos los archivos sin importar su extencion
            filetypes=[('Archivos de Texto', '*.txt'),('Todos los archivos','*.*'),('Archivos Python',('*.py','*.pyx'))]#muestra todos los archivos de texto
        )#pregunta donde queremos guardar el archivo nuevo
        if not self.archivo:
            return
        #si tenemos un archivo valido, lo abrimos en modo escritura 'w'
        with open(self.archivo,'w') as archivo:
            #leemos el contenido de la caja de texto
            text = self.campo_texto.get(1.0, tk.END)
            #escribimos el contenido al nuevo archivo
            archivo.write(text)
            #Cambiamos el nombre del archivo
            self.title(f'Editor Texto - {archivo.name}')
            #Indicamos que ya hemos abierto un archivo
            self.archivo_abierto = archivo



if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()


'''
Frame es una ventana invisibles, una ventana dentro de una ventana,
Permite administrar los componentes dentro del mismo frame 
ya que el grid si usamos demaciadas columnas se complicaria la configuracion,
se pueden agregar tantos frames como se requieran
'''
