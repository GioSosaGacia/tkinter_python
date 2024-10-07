'''
Creacion de usuario con tkinter con POO
'''

import tkinter as tk
from tkinter import ttk, messagebox
import sys

class LoginVentana(tk.Tk):

    def __init__(self):
        super().__init__()# hacemos la herencia de la clase Tk y su metodo __init__
        #Ventana Principal
        #ventana1 = tk.Tk() esta linea ya no se usa, ya que se creara el objeto a partir de la clase
        #Tamaño de la ventana. Cambiamos ventana1 por self al utilizar super()
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        #Para que no permita hacer cambios en la ventama principal en cuestiones de tamaño
        #con resizable
        self.resizable(0,0)#ejej x y eke y

        #configuracion del grid
        self.columnconfigure(0, weight=1) #La primera columna mantendra un ancho de 1
        self.columnconfigure(1,weight=3)#segunda columna con un ancho de 3

        #Creamos los componentes
        self._crear_componentes()

    #Definimos el metodos crear componentes: ES UN METODO DE instancia de la clase
    #utilizamos self cuando queremos usar variables que estan declaradas en otra seccion del codigo para utulizarlas en otra seccion donde no estan
    def _crear_componentes(self):
        #Usario
        etiqueta_usuario = tk.Label(self,text='Usuario: ')
        etiqueta_usuario.grid(row=0, column=0, sticky=tk.E, padx=5,pady=5)# ubicacion
        self.usuario_entrada = ttk.Entry(self, width=30)            #normal la habilita, se puede omitir ya que es su valor por defecto: state=tk.NORMAL
        self.usuario_entrada.grid(row=0, column=1,sticky=tk.W, padx=5, pady=5)

        #Password
        etiqueta_password = tk.Label(self,text='Contraseña: ')
        etiqueta_password.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)# ubicacion
        self.password_entrada = ttk.Entry(self, width=30, show='*')
        self.password_entrada.grid(row=1,column=1,sticky=tk.W, padx=5, pady=5)

        #boton login
        login_boton = ttk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3,column=0,columnspan=2) #Columnspan hace que agarre dos columna o el numero deseado

    def _login(self):
        messagebox.showinfo('Datos login', f'Usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}')
        '''
        entrada1.get()
        mensaje1 = entrada1.get()
        entrada2.get()
        mensaje2 = entrada2.get()
        if mensaje1:
             messagebox.showinfo('Mensaje informativo', 'Usuario: ' + mensaje1 + ' ' + 'Contraseña: ' + mensaje2 )
        else:
            messagebox.showerror('Ingresar datos' + 'Usuario' + mensaje1 + 'y' + mensaje2 + 'Contraseña' )'''

    #def salir():
     #   ventana1.quit()
      #  ventana1.destroy()
       # print('Salimos de la aplicación!!')
        #sys.exit()

#boton2 = ttk.Button(text='Salir', command=salir)
#boton2.grid(row=2,column=2,padx=5,pady=5)

#Ejecutar la ventana
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()



''' antes de la programacion orientada a objetos
import tkinter as tk
from tkinter import ttk, messagebox

# ventana principal
ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login')
ventana.iconbitmap('icono.ico')
ventana.resizable(0,0)

# configuración del grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

# usuario
usuario_etiqueta = ttk.Label(ventana, text='Usuario:')
usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
usuario_entrada = ttk.Entry(ventana)
usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

# password
password_etiqueta = ttk.Label(ventana, text='Password:')
password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
password_entrada = ttk.Entry(ventana, show='*')
password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

# boton Login
def login():
    messagebox.showinfo('Datos Login',
                        f'usuario: {usuario_entrada.get()}, Password: {password_entrada.get()}')

login_boton = ttk.Button(ventana, text='Login', command=login)
login_boton.grid(row=3, column=0, columnspan=2)

# Ejecutar la ventana
ventana.mainloop()'''
