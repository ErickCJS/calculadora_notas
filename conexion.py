import pymysql

def obtener_conexion():
    return pymysql.connect(
        host= 'calculador11-dsjulonerick-7a5a.l.aivencloud.com',
        port=13930,
        user= 'avnadmin',
        password= 'AVNS_BIpa-YQYdIrYqo0tK2u',
        db='calculadora' 
    )