# -*- coding: utf-8 -*-
#se lee el archivo y se ordena alfabeticamente
#en la matriz se guardan solo los nombres de peliculas y se eliminan los titulos repetidos
def opcion1():
    archivo=open("frases_de_peliculas.txt", encoding="utf-8")
    lista=archivo.readlines()
    lista=sorted(lista)
    lista2=[]
    for x in range(len(lista)):
        y,z = lista[x].split(';')
        lista2.append(z)
#creo una lista con los titulos sin repetir (Usando un set(elementos unicos))
    lista2 = list(set(lista2))
    for x in range(len(lista2)):
        print(str(x)+")",lista2[x])
def opcion2():
    import random
    archivo=open("frases_de_peliculas.txt", encoding="utf-8")
    lista=archivo.readlines()
    lista=sorted(lista)
#Se crea una matriz con [frase][nom pelicula] y la lista de nombres de peliclas
    matriz=[]
    lista2 =[]
    for x in range(len(lista)):
        y,z = lista[x].split(';')
        matriz.append(lista[x].split(';'))
        lista2.append(z) 
    lista2 = list(set(lista2))
#Se escoge una frase random y se muestra
    indice_f: = random.randint(0,55)
    resp = matriz[indice_f][1]
    op1 = random.choice(lista2)
    op2 = random.choice(lista2)
    lista= [resp,op1,op2]
    random.shuffle(lista)
    while op1 != op2:
        print(matriz[indice_f][0])
        print("A que pelicula pertence esta frase?")
        print("1)",lista[0])
        print("2)",lista[1])
        print("3)",lista[2])
        break
        respuesta=input()
    if respuesta == "1"
        if lista [0] == resp
            print("¡Felicitaciones! La respuesta es correcta.")
        else: 
            print("Respuesta incorrecta.")
    if respuesta == "2"
        if lista [1] == resp
            print("¡Felicitaciones! La respuesta es correcta.")
        else: 
            print("Respuesta incorrecta.")
    if respuesta == "3"
        if lista [2] == resp
            print("¡Felicitaciones! La respuesta es correcta.")
        else: 
            print("Respuesta incorrecta.")
    return matriz
