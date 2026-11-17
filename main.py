import funciones_principales as fc
from conexion import crear_tabla

crear_tabla()

while True:    
    print("SISTEMA DE GESTIÓN DE PRODUCTOS -Ver 0.9")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Salir del sistema")

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
            pass
     
        #Modificar producto
        case "4":
            pass
            
        #Eliminar producto                 
        case "5":
            fc.eliminar_producto()
            
        #Caso error        
        case _:
            print("Opcion invalida, intente denuevo.")
            continue
        