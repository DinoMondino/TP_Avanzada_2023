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
    indice_f=random.randint(0,55)
    print(matriz[indice_f][0])
    print("A que pelicula pertence esta frase?")
#utilizar la lista2 baja las posibilidades de que se repita la misma pelicula en las opciones
    lista= [matriz[indice_f][1],lista2[random.randint(0,53)],lista2[random.randint(0,53)]]
    random.shuffle(lista)
    print("1)",lista[0])
    print("2)",lista[1])
    print("3)",lista[2])
    respuesta=input()
    if respuesta in matriz[indice_f][1]:
        print("Correctou")
    else:
        print("Incorrecto")
