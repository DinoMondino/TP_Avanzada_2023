import operator
def lector(archivo_str):
  #Se abre el archivo y se extraen los datos en una lista
  archivo=open(archivo_str+".csv")
  lista=archivo.readlines()
  matriz=[]
  #Verifica si hay espacios despues de la fecha(6/7 or 7/8 caracter) y borra lo que esta
  #adelante hasta que encuentre una coma
  if((lista[1][6:7]==" ") or (lista[1][7:8]==" ")):
    for x in range(1,len(lista)):
      matriz.append(lista[x].split(' '))
      matriz[x-1][1] = matriz[x-1][1].split(',')[1]
      matriz[x-1][1] = matriz[x-1][1].strip('\n')
      matriz[x-1][1] = float(matriz[x-1][1])
  else:
    #Se separan los datos por coma y se guardan en una matriz
    for x in range(1,len(lista)):
      matriz.append(lista[x].split(','))
      matriz[x-1][1] = matriz[x-1][1].strip('\n')
      matriz[x-1][1] = float(matriz[x-1][1])
  #Se devuelven los datos en una matriz
  return matriz

def normalizar(archivo_str):
  #Llamamos a lector para que nos de la matriz
  matriz = lector(archivo_str)
  #Se buscan los max. y min. Se ordenan la matriz a conveniencia y se toma el primer valor.
  max=sorted(matriz, key=operator.itemgetter(1), reverse=True)[0][1]
  min=sorted(matriz, key=operator.itemgetter(1))[0][1]
  
  #Normalizamos los datos; max = 1; min = 0
  for x in range(0,len(matriz)):
    matriz[x][1] = (matriz[x][1] - float(min))/(float(max) - float(min)) 
    #print(matriz[x][1])
  #print("########################################################################")
  return matriz

#resist = max ; soporte = min
def resist_soporte(archivo_str):
    matriz = lector(archivo_str)
    #como los dos valores estan entre el dia 0 y 60
    #creo una matriz nueva con los 60 primeros valores
    matriz_60=[]
    for x in range(0,60):
        matriz_60.append(matriz[x][1])
    resistencia=sorted(matriz_60, reverse=True)[0]
    soporte=sorted(matriz_60)[0]
    return resistencia, soporte
  
def porcentaje(archivo_str):
    matriz=lector(archivo_str)
    inicial=matriz[0][1]
    for x in range(len(matriz)):
        matriz[x][1]=((matriz[x][1]-inicial)/inicial)*100
    
    matriz_60=[]
    for x in range(0,60):
        matriz_60.append(matriz[x][1])
    resistencia=sorted(matriz_60, reverse=True)[0]
    soporte=sorted(matriz_60)[0]
    return matriz, soporte, resistencia