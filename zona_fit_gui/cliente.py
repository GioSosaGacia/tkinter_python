#a esta clase se le conoce como de entidad o de dominio de la aplicacion ya que representa
# el tipo de informacion que se trabajara en nuestra aplicacion

class Cliente:

    def __init__(self,id=None,nombre=None,apellido=None,membresia=None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._membresia = membresia

    def __str__(self):
        return f'Id: {self._id}, nombre: {self._nombre},' \
               f' apellido: {self._apellido}, membresia: {self._membresia}'
    
