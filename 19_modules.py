import sys #modulo para el sistema operativo

print(sys.path)

import re #Modulo para las expreciones regulares

text = 'Mi numero de telefono es 6141581234, el codigo del pais es 52. Mi numero de la suerte es 7'

result = re.findall('[0-9]+',text) #Exprecion regular para encontrar numeros

print(result)

import time #Modulo para trabajar con horas y fechas

timestamp = time.time() #Fecha actual en formato 
local = time.localtime()
resultTime = time.asctime(local) #Imprimiendo la hora en formato humano

print(timestamp)
print(resultTime)

import collections #Modulo para trabajar con listas

numbers = [1,1,1,2,2,3,4,4,5,21]

counter = collections.Counter(numbers)#contando cuantas veces se repite un numero
print(counter)

