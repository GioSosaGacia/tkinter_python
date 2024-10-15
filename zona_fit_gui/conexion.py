from mysql.connector import pooling #nos permite tener un pool de conexiones
from mysql.connector import Error
class Conexion:

    DATABASE = 'zona_fit_db'
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = 'Uppercase1.'
    DB_PORT = '3306'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.pool is None:# se crea el objeto de pool
            try:  #creacion del objeto de pool de conexiones
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USER,
                    password=cls.PASSWORD
                )
                print(f'Nombre del pool: {cls.pool.pool_name}')
                print(f'Tamaño del pool: {cls.pool.pool_size}')
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener el pool: {e}')
        else:
            return cls.pool # faltaba el return por eso solo dejaba correr la aplicacion una vez en app zona fit
        #y depues marcaba error de conexion
#
    @classmethod
    def obtenerConexion(cls):#get conexion nos retorna un objeto de conexion a la base de datos
        return cls.obtenerPool().get_connection()#retornamos obtenerPool para asegurarnos que tenemos un objeto pool activo

    @classmethod
    def liberarConexion(cls,conexion):
        conexion.close()

if __name__ == '__main__':
    #creacion del objeto pool
    conexion1 = Conexion.obtenerPool()
    print(conexion1)

    #obtener un objeto de tipo conexion
    cnx1 = Conexion.obtenerConexion()
    print(cnx1)

    #cerrar una conexion y retornarla al pool
    Conexion.liberarConexion(cnx1)
    print(f'Se ha liberado la conexion')
    #cnx1.close() #nos permite cerrar la conexion obtenida a partir del pool para regresarla y este disponoble

