import sqlite3 as sql

#Crear conexion con el archivo
def conectar():
    conexion = sql.connect("productos.db")
    return conexion

#Crear tabla
def crear_tabla():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

    
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS registroProductos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            categoria TEXT
        )
        """)
        conexion.commit()
        print("Se ha creado la tabla con éxito")
    except sql.Error as Error:  
        print(f"Ha ocurrido el siguiente error: {Error}")
    finally:
        conexion.close()