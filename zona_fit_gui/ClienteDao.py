# es un patron de diseño, son soluciones ya conocidas a problemas que nos encontramos
#comunmente al crear aplicacion, cada patron es como un plano que podemos usar y personalizar para resolver un problema
#al diseñar una aplicacion
from zona_fit_gui.cliente import Cliente
from zona_fit_gui.conexion import Conexion


#DAO DATA ACCESS OBJECT
#este patron se utiliza para acceder a la informacion de un entidad de una aplicacion
#se encarga de administrar la infomacion de una tabla o entidad

class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre,apellido,membresia) VALUES(%s,%s,%s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMIAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            #mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0],registro[1],registro[2],registro[3])
                clientes.append(cliente)
            return  clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar los clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

    @classmethod
    def insertar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valores = (cliente._nombre,cliente._apellido,cliente._membresia)
            cursor.execute(cls.INSERTAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

    @classmethod
    def actualizar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valores = (cliente._nombre,cliente._apellido,cliente._membresia,cliente._id)
            cursor.execute(cls.ACTUALIZAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

    @classmethod
    def eliminar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valores = (cliente._id,)
            cursor.execute(cls.ELIMIAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)


if __name__ == '__main__':
    #Seleccionar clientes
    #clientes = ClienteDAO.seleccionar()
    #for cliente in clientes:
     #   print(cliente)

    #insertar
    #cliente1 = Cliente(nombre='MariCruz',apellido='Delgadillo',membresia=4)
    #clientes_insertados = ClienteDAO.insertar(cliente1)
    #print(f'Clientes insertado: {clientes_insertados}')

    #actualizar
    cliente_actualizar = Cliente(5,'Maria del Rosario','Sosa Garcia',33)
    clientes_actualizar = ClienteDAO.actualizar(cliente_actualizar)
    print(f'Clientes actualizados: {clientes_actualizar}')

    #eliminar
    #cliente_eliminar = Cliente(3)
    #clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    #print(f'Clientes eliminados: {clientes_eliminados}')
