import funciones_sql as sql
from conexion import conectar


#Agregar informacion
def registrar_producto():
    
        
    # Ingresar nombre    
    nombre_producto = input("Ingrese el nombre del producto: ").lower().strip()
    while nombre_producto == "":
        print("El nombre no puede estar vacio")
        nombre_producto = input("Ingrese el nombre del producto: ").lower().strip()

    # Ingresar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese el stock del producto: "))
                            
            if cantidad < 0:
                print("El valor ingresado no puede ser negativo.")
                continue
            else:
                break
        except ValueError:
            print("El valor ingresado debe ser un numero entero")
        
    # Ingresar descripcion
    descripcion = input("Ingrese la descripcion del producto: ").lower().strip()

    # Ingresar precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
                    
            if precio <= 0:
                print("El precio debe ser mayor a cero")
                continue
                    
            break
        except ValueError:
            print("Error: debe ingresar un numero")

    # Ingresar categoria
    categoria = input("Ingrese la categoria del producto: ").lower().strip()
    while categoria == "":
        print("La categoria no puede estar vacia")
        categoria = input("Ingrese la categoria del producto: ").lower().strip()

    sql.cargar_producto(nombre_producto, cantidad, descripcion, precio, categoria)
    
                                     
def mostrar_productos():    

    while True:    
        print("Seleccione como desea visualizar los productos:")
        print("1. Informacion completa")
        print("2. Informacion esencial")
        print("3. Volver al menu principal")
        

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            #Informacion completa (todas las columnas)
            case "1":
                lista = sql.obtener_productos()
                if len(lista) == 0:
                        print("No hay productos registrados.")
                else:
                    print("***TODOS LOS PRODUCTOS***")
                
                    for indice in range(len(lista)):
                        producto = lista[indice]
                
                        print(f"ID del producto: {producto[0]}.")
                        print(f"Nombre: {producto[1]}")
                        print(f"Cantidad: {producto[2]}")
                        print(f"Descripcion: {producto[3]}")
                        print(f"Precio: {producto[4]}")
                        print(f"Categoria: {producto[5]}")
                        print("\n")
                            
            #Informacion esencial (nombre, cantidad y precio)   
            case "2":
                lista_esencial = sql.obtener_productos_esencial()
                if len(lista_esencial) == 0:
                        print("No hay productos registrados.")
                else:
                    print("***INFORMACION ESENCIAL DE PRODUCTOS***")
                
                    for indice in range(len(lista_esencial)):
                        producto = lista_esencial[indice]
                                        
                        print(f"Nombre: {producto[0]}")
                        print(f"Cantidad: {producto[1]}")
                        print(f"Precio: {producto[2]}")
                        print("\n")

            case "3":
                break
                
                         
#Eliminar producto por id

def eliminar_producto():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        id = input("Escriba el id del producto a eliminar: ")
        #Verificar producto
        cursor.execute("""
            SELECT * FROM registroProductos
            WHERE id = ? 

        """,(id,))

        producto_a_eliminar = cursor.fetchone()

        #Submenu de confirmacion
        if producto_a_eliminar:
            print(f"Se ha encontrado el siguiente producto: {producto_a_eliminar}")
            print("Está seguro de que desea eliminarlo?")
            print("1. Si")
            print("2. No")

            decision = input("Seleccione una opcion: ")

            while True:    
                match decision:
                    case "1": 
                        cursor.execute("""
                        DELETE FROM registroProductos
                        WHERE id = ?

                    """,(id,))
                        conexion.commit()
                        if cursor.rowcount > 0:
                            print("Producto eliminado exitosamente")
                            break
                        else:
                            print("Producto no encontrado")
                            continue

                    case "2":
                        print("Volviendo al menu principal")
                        break

                    case _:
                        print("Opcion no valida, intente nuevamente")
                        continue
                    

            

        else:
            print("Producto no encontrado")
    except Exception as error:
            print(error)
    finally:
        conexion.close()    


def buscar_productos_por_id():
    try:
        id = int(input("Ingrese el ID del producto: "))
        producto = sql.obtener_producto_por_id(id)
        
        if producto:
           visualizar_productos([producto])
           return producto
        else:
            print("No se ha encontrado ningun producto.")
            return None
    except ValueError:
        print("Error: el ID debe ser un numero entero.")


#Funcion sin menu para utilizarse con busqueda por ID
def visualizar_productos(lista):
    if len(lista) == 0:
        print("No hay productos registrados.")
    else:
        print("***RESULTADO DE BUSQUEDA***")

        for indice in range(len(lista)):
            producto = lista[indice]

            print(f"ID: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Cantidad: {producto[2]}")
            print(f"Descripcion: {producto[3]}")
            print(f"Precio: {producto[4]}")
            print(f"Categoria: {producto[5]}")
            print("\n")