
pacientes = []

pacientes_mas_5 = []


def mostrar_menu():
    '''
    funcion que sirve para mostrar el menu 
    dependiendo la opcion llama distintas funciones
    si se elige una opcion incorrecta repite el bucle
    
    no recibe parametros ni retorna valores
    '''
    opcion = ""

    while opcion != "9":   
        print('''
1• Cargar paciente/s.
2• Mostrar todos los pacientes.
3• Buscar pacientes por historial clinico.
4• Ordenar pacientes por historial clinico.
5• Mostrar paciente con mas dias de internacion.
6. Mostrar paciente con menos dias de internacion.
7. Cantidad de pacientes con días de internación mayor a 5 días.
8. Promedio de internacion de todos los pacientes.
9. Salir del sistema

        ''')
            

        opcion = input("Ingrese la opcion deseada: ")

        match opcion:

            case "1":
                cargar_pacientes(pacientes)
        

            case "2":
                mostrar_pacientes(pacientes)

            case "3":
                realizar_busqueda(pacientes)

            case "4":
                organizar_pacientes(pacientes)
                mostrar_pacientes(pacientes)

            case "5":
                mostrar_mas_internado(pacientes)

            case "6":
                mostrar_menos_internado(pacientes)

            case "7":
                mostrar_pacientes_5_dias(pacientes)
                mostrar_pacientes(pacientes_mas_5)
                

            case "8":
                hacer_promedio_internacion(pacientes)

            case "9":
                print("Finalizando sistema...")
                return
            
            case _:
                print("Opcion erronea, ingrese nuevamente")


def cargar_pacientes(pacientes : list) -> None:
    '''
    funcion que recibe una lista por parametro

    permite cargar la cantidad de elementos que desee el usuario
    va modificando la lista de forma dinamica en un bucle
    
    no retorna valores
    '''
    
    respuesta = "s"
    while respuesta.lower() == "s":
           
        cantidad_pacientes = -1
                    
        while cantidad_pacientes < 1:
            
            cantidad_pacientes = input("Ingrese la cantidad de pacientes que carga: ") 

            if cantidad_pacientes.isdigit():
                
                cantidad_pacientes = int(cantidad_pacientes)
                        
            else:
                cantidad_pacientes = -1 

        for _ in range(cantidad_pacientes):
      
            historial_clinico = -1

            while historial_clinico < 1:
                historial_clinico = input("Ingrese el historial clinico del paciente: ")
                if historial_clinico.isdigit():
                    historial_clinico = int(historial_clinico)
                
                else:
                    historial_clinico = -1
            nombre_paciente = input("Ingrese el nombre del paciente: ").capitalize()
            
            edad_paciente = -1
           
            while edad_paciente < 1:
                edad_paciente = input("Ingrese la edad del paciente: ")
                if edad_paciente.isdigit():
                    edad_paciente = int(edad_paciente)
                else:
                    edad_paciente = -1
            diagnostico_paciente = input("Ingrese el diagnostico del paciente: ").capitalize()
            
            cantidad_internacion = -1
            
            while cantidad_internacion < 1:
                cantidad_internacion = input("Ingrese la cantidad de dias internado del paciente: ")
                if cantidad_internacion.isdigit():
                    cantidad_internacion = int(cantidad_internacion)
                else:
                    cantidad_internacion = -1
            
            pacientes.append([historial_clinico, nombre_paciente, edad_paciente, diagnostico_paciente, cantidad_internacion])
            print("Paciente cargado con exito")
        
        print("pacientes cargado con exito")
        
        respuesta = input("¿Desea cargar más productos (s/n)?: ").lower()
        
        while respuesta not in ["s", "n"]:
            
            respuesta = input("Respuesta no valida. Ingrese 's' para continuar o 'n' para salir: ").lower()

        


def mostrar_pacientes(pacientes : list) -> None:
    '''
    funcion que recibe una lista por parametro
    verifica que no este vacia y la recorre
    mostrando el contenido que esta dentro de ella

    no retorna ningun valor
    '''
    
    if len(pacientes) > 0:

        for i in range(len(pacientes)):
            
            nombre = pacientes[i][1]
            historial_clinico = pacientes[i][0]
            edad = pacientes[i][2]
            diagnostico = pacientes[i][3]
            dias_internado =pacientes[i][4]
            
            print(f"Nombre del paciente: {nombre}, Historial: {historial_clinico}, Edad: {edad},Diagnostico:{diagnostico}, Dias de internacion {dias_internado}  ")

    else:
        print(f"Todavia no se han cargado pacientes al sistema")



def realizar_busqueda(pacientes : list) -> None:
    '''
    funcion que recibe una lista como parametro.

    Esta función permite al usuario realizar una busqueda de un elemento
    verifica que la lista no este vacia y la recorre.
    muestra en pantalla un mensaje de resultado

    no retorna valores.
    '''
    
    if len(pacientes) > 0:
        
        paciente_busqueda = -1
        
        while paciente_busqueda < 0:

            paciente_busqueda = input(f"Ingrese el numero de historial del paciente a buscar: ")
            
            if paciente_busqueda.isdigit():

                paciente_busqueda = int(paciente_busqueda)

            else:
                paciente_busqueda = -1
            
        for i in range(len(pacientes)):
                    
            if pacientes[i][0] == paciente_busqueda:

                print(f"El paciente {pacientes[i][1]} con historial {pacientes[i][0]} tiene {pacientes[i][2]} años, su diagnostico es {pacientes[i][3]} y esta internado hace {pacientes[i][4]} dias ")
                return
                        
        print(f"No se encontro el historial {paciente_busqueda}")
                

            
    else:
        print(f"No hay pacientes cargados aun")

def organizar_pacientes(pacientes : list) -> None:
    '''
    funcion que recibe una lista como parametro

    verifica que no este vacia y la recorre
    Organiza la lista por el historial de los pacientes en orden ascendente.

    no retorna valores.
    '''


    if len(pacientes) > 0:

        numero = len(pacientes)
        
        for i in range(numero -1):
            for j in range(0, numero-i-1):
                if pacientes[j][0] > pacientes[j+1][0]:
                    pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]

    else:
        print(f"No hay pacientes cargados aun") 

def mostrar_mas_internado(pacientes : list) -> None:
    '''
    funcion que recibe una lista como parametro

    verifica que no este vacia y la recorre
    compara cada elemento de la lista
    muestra el paciente con mas dias de internacion

    no retorna valores.
    '''
    if len(pacientes) > 0:

        paciente_mas_internado = pacientes[0]

        for paciente in pacientes:
            if paciente[4] > paciente_mas_internado[4]:

                paciente_mas_internado = paciente
            
            
        print(f"El paciente con mayor dias de internacion es: {paciente_mas_internado[1]} con {paciente_mas_internado[4]} dias de internacion")


        
       




    else:
        print(f"No hay pacientes cargados aun") 
    
def mostrar_menos_internado(pacientes : list) -> None:

    '''
    funcion que recibe una lista como parametro

    verifica que no este vacia y la recorre
    compara cada elemento de la lista
    muestra el paciente con mas dias de internacion

    no retorna valores.
    '''

    if len(pacientes) > 0:

        paciente_menos_internado = pacientes[0]

        for paciente in pacientes:
            if paciente[4] < paciente_menos_internado[4]:

                paciente_menos_internado = paciente
            
            
        print(f"El paciente con menos dias de internacion es: {paciente_menos_internado[1]} con {paciente_menos_internado[4]} dias de internacion")


        
       




    else:
        print(f"No hay pacientes cargados aun")

def mostrar_pacientes_5_dias(pacientes : list) -> None:

    '''
    funcion que recibe una lista como parametro
    
    verifica que no este vacia y la recorre
    compara cada elemento de la lista en su ultimo indice
    modifica la lista pacientes_mas_5 segun la condicion se cumpla

    no retorna valores.
    '''

    internacion_minima = 5

    if len(pacientes) > 0:

        for i in range(len(pacientes)):

            if pacientes[i][4] > internacion_minima:

                pacientes_mas_5.append([pacientes[i][0],pacientes[i][1],pacientes[i][2],pacientes[i][3],pacientes[i][4]])


                
                
    
        

    else:
        print(f"No hay pacientes cargados aun")

def hacer_promedio_internacion(pacientes : list) -> None:
    '''
    recibe una lista por parametro
    
    verifica que no este vacia y la recorre
    realiza el promedio y lo muestra en pantalla

    no retorna ningun valor
    '''

    if len(pacientes) > 0:
    
        acumulador_internacion = 0
        cantidad_pacientes = 0
    

        for internacion in pacientes:

            acumulador_internacion += internacion[4]
            cantidad_pacientes += 1

        

        promedio_internacion = acumulador_internacion / cantidad_pacientes
        
        print(f"El promedio de dias de internacion es {promedio_internacion} por los {cantidad_pacientes} pacientes")
        
        
    else:
        print("Todavia no se han cargado pacientes al sistema")

mostrar_menu()
