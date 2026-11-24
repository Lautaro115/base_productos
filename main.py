import funciones_principales as fc
from conexion import crear_tabla

crear_tabla()

while True:    
    print("SISTEMA DE GESTIÓN DE PRODUCTOS -Ver 0.9")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por ID")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Reporte de stock bajo")
    print("7. Eliminar todos los datos")
    print("8. Salir del sistema")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        #Agregar producto
        case "1":
            fc.registrar_producto()
                        
        #Mostrar productos    
        case "2":            
            fc.mostrar_productos()

        #Buscar producto
        case "3":
            fc.buscar_productos_por_id()
     
        #Modificar producto
        case "4":
            fc.actualizar_producto_por_id()
            
        #Eliminar producto                 
        case "5":
            fc.eliminar_producto()

        #Reporte stock
        case "6":
            fc.reporte_stock()

        #Eliminar todos los datos (usar con precaucion)
        case "7":
            fc.eliminar_datos_tabla()

        #Salir del sistema
        case "8":
            print("Saliendo del sistema...")
            break        
            
        #Caso error        
        case _:
            print("Opcion invalida, intente denuevo.")
            continue
        