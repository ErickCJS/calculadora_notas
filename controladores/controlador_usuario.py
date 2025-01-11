from flask import Flask, render_template, request, redirect, url_for, flash
from conexion import obtener_conexion
from pymysql import MySQLError

def listar_usuarios():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor :
        cursor.execute('select * from usuario')
        usuarios = cursor.fetchall()
    print(usuarios)
    conexion.close()
    return usuarios

def insertar_usuario(nombre_apellido, tipo_usuario, imagen, password, correo):
    conexion = obtener_conexion()
    
    if conexion is None:
        raise Exception("No se pudo establecer la conexión a la base de datos.")
    
    try:
        cursor = conexion.cursor()
        query = """INSERT INTO usuario (nombre_apellido, tipo_usuario, enlace_imagen, contraseña, correo)
                   VALUES (%s, %s, %s, %s, %s)"""
        datos = (nombre_apellido, tipo_usuario, imagen, password, correo)
        
        cursor.execute(query, datos)
        conexion.commit()  # Confirmar los cambios

        print("Usuario registrado exitosamente.")
    except MySQLError as e:
        print(f"Error al insertar usuario: {e}")
        raise
    finally:
        # Cerrar cursor y conexión
        if conexion:
            cursor.close()
            conexion.close()
