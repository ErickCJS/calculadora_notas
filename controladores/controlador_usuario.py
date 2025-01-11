from conexion import obtener_conexion

def listar_usuarios():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor :
        cursor.execute('select * from usuario')
        usuarios = cursor.fetchall()
    print(usuarios)
    conexion.close()
    return usuarios