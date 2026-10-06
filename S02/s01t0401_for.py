"""
Escribir un programa que calcule
la suma de los "n" numeros naturales.
Por ejemplo si n= 100, el programa
calculara la suma de 1 al 100
42

"""

#importar la biblioteca de tiempo
import time

#Crear las variables para el problema
n = 100
#Como ya existe sum, se cambiara el name
the_sum = 0

#Tomando el tiempo 1
timestamp_01 = time.time()

#Iniciando la suma
while(n > 0):
    the_sum = the_sum + n #100 + 99 + 98.. + 1
    n = n - 1
timestamp_02 = time.time()    
# imprimimoas

# Imprimimos la solución 
print(f"la suma es (the_sum)")

# Calculamos el tiempo
elapsed_time = round((timestamp_02-timestamp_01) * 1e6,2)
print(f"tiempo de ejecucion: {elapsed_time}us")