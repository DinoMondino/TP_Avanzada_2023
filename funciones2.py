# -*- coding: utf-8 -*-
#se lee el archivo y se ordena alfabeticamente
#en la matriz se guardan solo los nombres de peliculas y se eliminan los titulos repetidos
def opcion1():
    archivo=open("frases_de_peliculas.txt", encoding="utf-8")
    lista=archivo.readlines()
    lista=sorted(lista)
    matriz=[]
    for x in range(len(lista)):
        if lista[x] == lista[x+1]:
            lista.pop(x)
    for x in range(len(lista)):
        matriz.append(lista[x].split(';'))   
        print(str(x)+")",matriz[x][1])
        
def opcion2():
    import random
    archivo=open("frases_de_peliculas.txt", encoding="utf-8")
    lista=archivo.readlines()
    lista=sorted(lista)
    matriz=[]
    for x in range(len(lista)):
        matriz.append(lista[x].split(';'))   
    indice_f=random.randint(0,55)
    print(matriz[indice_f][0])
    print("A que pelicula pertence esta frase?")
    lista= [matriz[indice_f][1],matriz[random.randint(0,55)][1],matriz[random.randint(0,55)][1]]
    random.shuffle(lista)
    print("1)",lista[0])
    print("2)",lista[1])
    print("3)",lista[2])
    respuesta=input()
    if respuesta in matriz[indice_f][1]:
        print("Correctou")
    else:
        print("Incorrecto")