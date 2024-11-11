import time # Se utiliza el import time para utilizar time.sleep() para darle mas realismo a la bilbioteca

# Se definen estaticamente los libros y un diccionario libros para guardar estos ahí, ya que facilitará el acceso a ellos.
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
    print()

# La función ver_catalogo() contiene un for que recorre el diccionario libros y muestra por pantalla el titulo y autor de cada libro
def ver_catalogo():
    for i in libros:
        print("————————————————————————————————————————————————————————")
        print(f"Libro {i}: {libros[i]['Titulo']} | Autor: {libros[i]['Autor']}")
        print("————————————————————————————————————————————————————————")
    print("")
    input("Presione Enter para continuar... ")
    print("")

# La función consultar_disponibilidad() muestra por pantalla el titulo y autor del libro que el usuario quiere consultar, también verifica si 
# este libro existe mediante el true y false.
def consultar_disponibilidad():
    opcion_disp = input("¿Qué libro desea consultar? \n")
    existe = False
    for i in libros:
        if libros[i]["Titulo"].upper() == opcion_disp.upper():
            existe = True

            if libros[i]["Disponibilidad"] == True:
                print(f"El libro '{libros[i]['Titulo']}' está disponible.")
                input("Presione Enter para continuar... ")
                print("")
            else:
                print(f"El libro '{libros[i]['Titulo']}' no está disponible.")
                input("Presione Enter para continuar... ")
                print("")
            
            break
    if existe == False:
        print("Ese libro no se encuentra en el catálogo.")
        print("Inténtelo de nuevo.")
        input("Presione Enter para continuar... ")
        print("")
        reserva()
    print("")

# La función reserva() muestra por pantalla el titulo y autor del libro que el usuario quiere reservar, también verifica si este está
# disponible mediante el true y false.
def reserva():
    print("")
    opcion_reserva = input("¿Que libro quieres reservar? \n")
    existe = False
    for i in libros:
        if libros[i]["Titulo"].upper() == opcion_reserva.upper():
            existe = True

            if libros[i]["Disponibilidad"] == True:
                print(f"El libro '{libros[i]['Titulo']}' está disponible.")
                print("Reservando libro...")
                print("")
                time.sleep(2)
                libros[i]["Disponibilidad"] = False
                print(f"Se ha reservado exitosamente el libro '{libros[i]["Titulo"]}'")
                input("Presione Enter para continuar... ")
                print("")
            else:
                print(f"El libro '{libros[i]['Titulo']}' no está disponible.")
                input("Presione Enter para continuar... ")
                print("")
            
            break
    if existe == False:
        print("Ese libro no se encuentra en el catálogo.")
        print("Inténtelo de nuevo.")
        input("Presione Enter para continuar... ")
        print("")
        reserva()
    print("")

# La función salir() muestra un mensaje de agradecimiento y cierra el programa.
def salir():
    print("Gracias por usar nuestro servicio. Saliendo de la Biblioteca...")
    exit()

# Llamamos a la función menu para que antes de ejecutar el while (opciones a introducir) muestre el menú al usuario
menu()

# Bucle while que pregunta al usuario que opción quiere usar y ejecuta la función correspondiente según la opción que elija
while True:
    opcion = input("¿Qué acción desea realizar?: ").upper()
    if opcion == "V":
        ver_catalogo()
        menu()
    elif opcion == "C":
        consultar_disponibilidad()
        menu()
    elif opcion == "R":
        reserva()
        menu()
    elif opcion == "S":
         salir()
    else:
        print("Opción no válida, intente de nuevo")
        menu()
