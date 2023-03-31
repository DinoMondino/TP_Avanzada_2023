from funciones2 import opcion1,opcion2
five = "false"
while five == "false":
     with open ("opciones.txt", "a") as opc:
        print("""
              #######################################
    #  Películas: Preguntas y respuestas  #
    #######################################
    Elige una opción
    1 - Mostrar lista de películas.
    2 - ¡Trivia de película!
    3 - Mostrar secuencia de opciones seleccionadas previamente.
    4 - Borrar historial de opciones.
    5 - Salir
    """)
        choosen = input(print("Eliga su opción:"))
        opc.write(choosen + "\n")
        if choosen == "1":
            opcion1()
        elif choosen == "2":
            opcion2()
        elif choosen == "3":
            opc.close()
            opc = open("opciones.txt")
            lista=opc.readlines()
            for x in lista:
              print(x)
        elif choosen == "4":
          opc.close()
          opc = open("opciones.txt","w")
        elif  choosen == "5":
          print("Gracias por jugar <3")
          five = "true"
        else:
          print("La opción ingresada no es correcta.")
