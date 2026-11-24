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

def actualizar_producto_por_id():
    producto = buscar_productos_por_id() 
    
    if producto:
        print("Seleccione lo que desee actualizar:")
        print("1. Actualizar nombre")
        print("2. Actualizar stock")
        print("3. Actualizar descripcion")
        print("4. Actualizar precio")
        print("5. Actualizar categoria")
        
        opcion = input("Seleccione la opcion deseada: ")
        
        match opcion:
            case "1":
                # actualizar nombre
                nombre = input("Ingrese el nuevo nombre del producto: ").lower().strip()
                while nombre == "":
                    print("El nombre no puede estar vacio")
                    nombre = input("Ingrese el nombre del producto: ").lower().strip()
                
                sql.actualizar_nombre(producto[0],nombre)
                print("El nombre del producto ha sido actualizado")
            
            case "2":
                # actualizar stock
                while True:
                    try:
                        cantidad = int(input("Ingrese el nuevo stock del producto: "))
                        
                        if cantidad < 0:
                            print("El valor ingresado no puede ser negativo.")
                            continue
                        else:
                            break
                    except ValueError:
                        print("El valor ingresado debe ser un numero entero")
                    
                sql.actualizar_cantidad(producto[0],cantidad)
                print("El stock del producto ha sido actualizado")

            case "3":
                # actualizcar descripcion
                descripcion = input("Ingrese la nueva descripcion del producto: ").lower().strip()
                 
                sql.actualizar_descripcion(producto[0],descripcion)  
                print("La descripcion del producto ha sido actualizada")

            case "4":
                # actualizar precio
                while True:
                    try:
                        precio = int(input("Ingrese el nuevo precio del producto: "))
                        
                        if precio <= 0:
                            print("El precio debe ser mayor a cero")
                            continue
                        
                        break
                    except ValueError:
                        print("Error: debe ingresar un numero entero")
                        
                sql.actualizar_precio(producto[0],precio)
                print("El precio del producto ha sido actualizado")

            case "3":
                # actualizar categoria
                categoria = input("Ingrese la nueva categoria del producto: ").lower().strip()
                while categoria == "":
                    print("La categoria no puede estar vacia")
                    categoria = input("Ingrese la nueva categoria del producto: ").lower().strip()
                
                sql.actualizar_categoria(producto[0],categoria)
                print("La categoria del producto ha sido actualizada")

def eliminar_producto():
    #Eliminar producto
    try:
        id_producto = int(input("Ingrese el id del producto que desea eliminar: ")) 
        
        if id_producto <= 0:
            print("Error: el ID debe ser numero entero positivo") 
            return
        
        producto = sql.obtener_producto_por_id(id_producto)
        
        if not producto:
            print("El producto no existe.")
            return
        
        confirmacion = input(f"Confirma eliminar {producto[1]} (s/n): ").lower().strip()
        
        if confirmacion != "s":
            print("Eliminacion cancelada")
            return
        
        if sql.eliminar_producto_por_id(id_producto):
            print(f"Se ha eliminado: {producto[1]} correctamente.")
        else:
            print("No se pudo eliminar el producto")

    except Exception as error:
       print(f"Ha ocurrido un error: {error}.")

def reporte_stock():
    #Comprobacion del limite
    while True:
        try:
            limite = int(input("Ingrese el limite de cantidad: "))
            if limite < 0:
                print("El limite no puede ser negativo.")
                continue
            
            break
        except ValueError:
            print("Error: el numero debe ser entero.")
        
    productos = sql.obtener_stock_bajo(limite)
    
    if not productos:
        print(f"No hay productos con stock igual o inferior a {limite}")
    else:
        print(f"***REPORTE DE STOCK (CANTIDAD <= {limite})***")
        visualizar_productos(productos)

def eliminar_datos_tabla():
    try:
        print("***¡ATENCION!***")
        print("Esta a punto de eliminar todos los datos de la tabla.")
        decision_eliminar = input("¿Esta seguro de que desea proceder? (s/n)").strip().lower()

        if decision_eliminar != "s":
            print("Eliminacion cancelada, volviendo al menu principal.")
            return

        else:
            if sql.vaciar_tabla():
                print("La tabla se ha vaciado correctamente.")

            else:
                ("No se ha hecho ninguna modificacion en la tabla.")
    except Exception as error:
        print(f"Ha ocurrido un error al eliminar los datos: {error}")
       


