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
        
        cursor.execute("SELECT * from registroProductos")
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
        
        cursor.execute("SELECT nombre_producto, cantidad, precio from registroProductos")
        return cursor.fetchall()
    except Exception as error:
        print(f"Error al obtener los productos: {error}")
        return []
    finally:
        conexion.close()

def obtener_producto_por_id(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM registroProductos WHERE id = ?",(id,))
        return cursor.fetchone()
    except Exception as error:
        print(f"Se ha producido el siguiente error: {error}")
        return None
    finally:
        conexion.close()

def actualizar_nombre(id_producto,nombre_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE registroProductos
            SET nombre_producto = ?
            WHERE id = ?                            
        """,(nombre_nuevo,id_producto))
        
        conexion.commit()
    except Exception as error:
        print(f"Error al actulizar el producto: {error}")
    finally:
        conexion.close()

def actualizar_cantidad(id_producto,cantidad_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE registroProductos
            SET cantidad = ?
            WHERE id = ?                            
        """,(cantidad_nuevo,id_producto))
        
        conexion.commit()
    except Exception as error:
        print(f"Error al actulizar el producto: {error}")
    finally:
        conexion.close()

def actualizar_descripcion(id_producto,descripcion_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE registroProductos
            SET descripcion = ?
            WHERE id = ?                            
        """,(descripcion_nuevo,id_producto))
        
        conexion.commit()
    except Exception as error:
        print(f"Error al actulizar el producto: {error}")
    finally:
        conexion.close()

def actualizar_categoria(id_producto,categoria_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE registroProductos
            SET categoria = ?
            WHERE id = ?                            
        """,(categoria_nuevo,id_producto))
        
        conexion.commit()
    except Exception as error:
        print(f"Error al actulizar el producto: {error}")
    finally:
        conexion.close()
        
def actualizar_cantidad(id_producto,cantidad_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE registroProductos
            SET cantidad = ?
            WHERE id = ?                            
        """,(cantidad_nuevo,id_producto))
        
        conexion.commit()
    except Exception as error:
        print(f"Error al actulizar el producto: {error}")
    finally:
        conexion.close()

def actualizar_precio(id_producto,precio_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE registroProductos
            SET precio = ?
            WHERE id = ?                            
        """,(precio_nuevo,id_producto))
        
        conexion.commit()
    except Exception as error:
        print(f"Error al actualizar el producto: {error}")
    finally:
        conexion.close()

def eliminar_producto_por_id(id_producto):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM registroProductos WHERE id = ?",(id_producto,))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as error:
        print(f"Error al eliminar el producto: {error}")
        return False
    finally:
        conexion.close() 

def obtener_stock_bajo(limite):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("""
            SELECT * FROM registroProductos
            WHERE cantidad <= ?
            ORDER BY cantidad ASC, id ASC         
        """,(limite,))
        return cursor.fetchall()
    except Exception as error:
        print(f"Ha ocurrido un error: {error}")
        return []
    finally:
        conexion.close()

def vaciar_tabla():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM registroProductos")                           
                    
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as error:
        print(f"Error al vaciar la tabla: {error}")
    finally:
        conexion.close()