'''
Frame es una ventana invisibles, una ventana dentro de una ventana,
Permite administrar los componentes dentro del mismo frame
ya que el grid si usamos demaciadas columnas se complicaria la configuracion,
se pueden agregar tantos frames como se requieran
'''
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')
ventana.iconbitmap('user.ico')
#grid de la ventana
ventana.columnconfigure(0, weight=1)#Para que ocupe todo el espacio de la ventana en fila y columna
ventana.rowconfigure(0, weight=1)

#Creamos estilos con ttk
estilos = ttk.Style()
#permite aplicar estilos(theme use), filedbackgroung modifica el color de las cajas de texto
#theme_use('clam') en tkinter se utiliza para controlar el aspecto de los widgets de una aplicación por defecto,
# utilizando el estilo de ese tema que corresponda a la clase de widget.
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white',
                  fieldbackground='black') #foreground modifica el color de la letra

#tbutton es la clase que se utilliza para agregar stilo a los botones
estilos.configure('TButton', background='#005f73')
estilos.map('TButton', background=[('active', '#0a9396')]) #map Consulta o establece valores dinámicos de opciones específicas en style.

#agregamos un frame que es un contenedor invisible
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

#titulo
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)
#usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario')
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

#password
password_etiqueta = ttk.Label(frame, text='Password')
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
password_caja_texto = ttk.Entry(frame,show='*')
password_caja_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

#BOTON
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

#event daa conocer el evento que se ejecuto
def validar(event):
    usuario = usuario_caja_texto.get()
    password = password_caja_texto.get()
    #usuario y password = admin  son los valores correctos
    if usuario == 'root' and password == 'admin':
        showinfo(title='Login', message='Datos correctos!!')
    else:
        showerror(title='Login', message='Datos incorrectos!')



#otra manera de aociar eventos/funciones a los botones
#bind nos permite ejecutar eventos entre '<>', bind no solo permite asociar un evento, si no varios al mismo tiempo
login_boton.bind('<Return>', validar)#Return es el evento que se aplica al presionar enter
login_boton.bind('<Button-1>',validar)#'<Button-1>' activa el metodo presionando click izquierdo del mouse


#publicamos el frame
frame.grid(row=0, column=0)


if __name__ == '__main__':
    ventana.mainloop()
