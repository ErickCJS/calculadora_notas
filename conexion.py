import pymysql
from pymysql import MySQLError

def obtener_conexion():
    try:
        conexion = pymysql.connect(
            host='calculador11-dsjulonerick-7a5a.l.aivencloud.com',
            port=13930,
            user='avnadmin',
            password='AVNS_BIpa-YQYdIrYqo0tK2u',
            db='calculadora',
        )
        print('Conexión exitosa a la base de datos')
        return conexion
    except MySQLError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
