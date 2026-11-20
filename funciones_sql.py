from conexion import conectar
import sqlite3 as sql


def cargar_producto(nombre_producto, cantidad, descripcion, precio, categoria):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO registroProductos (nombre_producto, cantidad, descripcion, precio, categoria)
        VALUES (?,?,?,?,?)        
        """,(nombre_producto, cantidad, descripcion, precio, categoria))

        conexion.commit()
        print("Producto agregado correctamente")

    except sql.Error as error:
        print(f"Ha ocurrido el siguiente error: {error}")
    finally:
        conexion.close()


        
def obtener_productos():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * from productos")
        return cursor.fetchall()
    except Exception as error:
        print(f"Error al obtener los productos: {error}")
        return []
    finally:
        conexion.close()


def obtener_productos_esencial():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT nombre_producto, cantidad, precio from productos")
        return cursor.fetchall()
    except Exception as error:
        print(f"Error al obtener los productos: {error}")
        return []
    finally:
        conexion.close()