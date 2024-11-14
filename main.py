import time  # Se utiliza el import time para utilizar time.sleep() para darle mas realismo a la bilbioteca
import os # Importamos el módulo os para realizar el clear de la terminal en una función más adelante

# Se definen estaticamente los libros y un diccionario libros para guardar estos ahí, 
# ya que facilitará el acceso a ellos.
Solo_Leveling = {
    "Titulo": "Solo Leveling",
    "Autor": "Chu-Gong",
    "Disponibilidad": True,
}

El_Libro_Troll = {
    "Titulo": "El Libro Troll",
    "Autor": "El Rubius",
    "Disponibilidad": True,
}

Juujika_no_rokunin = {
    "Titulo": "Juujika No Rokunin",
    "Autor": "Shiryuu Nakatake",
    "Disponibilidad": True,
}

libros = {
    1: Solo_Leveling,
    2: El_Libro_Troll,
    3: Juujika_no_rokunin,
}

# Esta función muestra por pantalla el menú como tal al usuario
def menu():
    print("===========[ Bienvenido a la Biblioteca de Daniel Cobo ]===========")
    print("(V) Ver catálogo de libros")
    print("(C) Consultar disponibilidad de un libro")
    print("(R) Reservar un libro")
    print("(S) Salir - Salir del programa")
    print("=============================================================")
    print("")

# La función ver_catalogo() contiene un for que recorre el diccionario libros y muestra por pantalla el titulo y autor de cada libro
def ver_catalogo():
    for i, libro in libros.items():
        print("————————————————————————————————————————————————————————")
        print(f"Libro {i}: {libro['Titulo']} | Autor: {libro['Autor']}")
        print("————————————————————————————————————————————————————————")
    print("")
    input("Presione Enter para continuar... ")
    print("")

# Función que comprueba si un libro está en el catálogo, devuelve el índice si lo encuentra y si no, devuelve False.
def comprueba_libro(titulo):
    for i in libros:
        if libros[i]['Titulo'].upper() == titulo.upper():
            return i
    return False

# La función consultar_disponibilidad() muestra por pantalla el titulo y autor del libro que el usuario quiere consultar, también verifica si 
# este libro existe mediante el true y false.
def consultar_disponibilidad():
    opcion_disp = input("¿Qué libro desea consultar? \n").upper()
    indice_libro = comprueba_libro(opcion_disp)
    if indice_libro != False:
        if libros[indice_libro]['Disponibilidad'] == True:
            print(f"El libro '{libros[indice_libro]['Titulo']}' está disponible para reservar.")
            input("Presione Enter para continuar... ")
        else:
            print(f"El libro '{libros[indice_libro]['Titulo']}' no está disponible para reservar.")
            input("Presione Enter para continuar... ")
    else:
        print("Ese libro no se encuentra en el catálogo. Inténtelo de nuevo.")
        input("Presione Enter para continuar... ")
        print("")
        consultar_disponibilidad()

    print("")

# La función reserva() muestra por pantalla el titulo y autor del libro que el usuario quiere reservar, también verifica si este está
# disponible mediante el true y false.
def reserva():
    opcion_reserva = input("¿Qué libro quieres reservar? \n").upper()
    indice_libro = comprueba_libro(opcion_reserva)
    if indice_libro != False:   
        if libros[indice_libro]['Disponibilidad'] == True:
            print(f"El libro '{libros[indice_libro]['Titulo']}' está disponible.")
            print("Reservando libro...")
            time.sleep(2)
            libros[indice_libro]["Disponibilidad"] = False
            print(f"Se ha reservado exitosamente el libro '{libros[indice_libro]['Titulo']}'")
            input("Presione Enter para continuar... ")
        else:
            print(f"El libro '{libros[indice_libro]['Titulo']}' no está disponible para reservar.")
            input("Presione Enter para continuar... ")
    else:
        print("Ese libro no se encuentra en el catálogo. Inténtelo de nuevo.")
        input("Presione Enter para continuar... ")
        print("")
        reserva()
    print("")

# La función salir() muestra un mensaje de agradecimiento y cierra el programa.
def salir():
    print("Gracias por usar nuestro servicio.\nSaliendo de la Biblioteca...")
    exit()

# Función que limpia la terminal del usuario para hacerla más visible
def limpiar():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux y Mac
        os.system('clear')

limpiar() # Limpiamos la terminal cuando se ejecute el codigo

# Llamamos a la función menu para que antes de ejecutar el while (opciones a introducir) muestre el menú al usuario
menu()

# Bucle while que pregunta al usuario que opción quiere usar y ejecuta la función correspondiente según la opción que elija
while True:
    opcion = input("¿Qué acción desea realizar?: ").upper()
    if opcion == "V":
        ver_catalogo()
        limpiar()
        menu()
    elif opcion == "C":
        consultar_disponibilidad()
        limpiar()
        menu()
    elif opcion == "R":
        reserva()
        limpiar()
        menu()
    elif opcion == "S":
        salir()
    else:
        print("Opción no válida, intente de nuevo")
        limpiar()
        menu()