from conexion import obtener_conexion

def verificar_usuario(correo, password):
    conexion = obtener_conexion()
  
    try:
        with conexion.cursor() as cursor:
            cursor.execute('''
                                select id_usuario,nombre_apellido,tipo_usuario, enlace_imagen,veces from usuario where correo = %s and contraseña = %s
                                ''', (correo,password))
            usuario = cursor.fetchone()

            if(usuario):
                veces = usuario[4] + 1
                cursor.execute('''
                    update usuario set veces = %s  where id_usuario = %s
                               ''', (veces, usuario[0]))

                conexion.commit()
                return usuario
            else:
                return False
    except:
        return False
    finally:
        conexion.close()


def listar_usuarios():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor :
        cursor.execute('select * from usuario')
        usuarios = cursor.fetchall()
    print(usuarios)
    conexion.close()
    return usuarios