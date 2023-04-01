# -*- coding: utf-8 -*-

from funciones import normalizar, resist_soporte
from funciones import porcentaje, lector


datos_g=lector("google")
datos_n=lector("nike")

matriz_g=normalizar("google")
matriz_n=normalizar("nike")

porcentaje_g,soporte_p_g, resist_p_g=porcentaje("google")
porcentaje_n,soporte_p_n, resist_p_n=porcentaje("nike")

resis_g, soporte_g=resist_soporte("google")
resis_n, soporte_n=resist_soporte("nike")

#calculo caida
caida_google=((soporte_g-resis_g)/resis_g)*100
caida_nike=((soporte_n-resis_n)/resis_n)*100

print("Caida google-.", caida_google,
      "Caida nike:", caida_nike)
"""
¿Se corresponde aproximadamente el valor calculado en el punto anterior con la caída para Google en el gráfico de la derecha? Justificar.
En el gráfico se observa que el máximo del dia aprox.32 se encuentra en un valor de 10% mayor al valor inicial, y el mínimo del dia aprox.50 
toma un valor cercano a -20%. Por lo que el valor obtenido de -30%de caida resulta congruente al valor aproximado de la gráfica.
"""
#calculo repunte
cant_datos_g=len(datos_g)
cant_datos_n=len(datos_n)

#repunte con datos normales
repunte_g=((datos_g[cant_datos_g-1][1]-soporte_g)/soporte_g)*100
repunte_n=((datos_n[cant_datos_n-1][1]-soporte_n)/soporte_n)*100

print("repuntes",repunte_g, repunte_n)
"""
¿Se corresponde aproximadamente el valor calculado en el punto anterior con el repunte para Google en el gráfico de la derecha? Justificar.
Para google, en el gráfico se observa que el mínimo se encuentra en un valor de -20% respecto al valor inicial y el último valor de la gráfica es cercano a 30%.
Por lo que el valor obtenido de 65% de repunte resulta ligeramente mayor al valor aproximado de la gráfica (50%).
"""

grafica("google")
grafica("nike")
superposicion()
