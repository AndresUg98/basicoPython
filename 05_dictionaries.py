##GENERANDO DICCIONARIO NORMAL



dict = {}

for element in range(1,11):
    dict[element] = element*2

print(dict)

#DICTIONARY COMPRENHENSION

dict_2= {element:element*2 for element in range(1,11)}

print(dict_2)

#MEZCLANDO LISTAS Y DICCIONARIOS
import random
countries=['col', 'mex', 'bol', 'pe']

population={}
for country in countries:
    population[country]= random.randint(1,100)

print(population)

##Usando DICTIONARY COMPRENHENSION CON LISTAS

import random
countries=['col', 'mex', 'bol', 'pe']

population_v2={country:random.randint(1,100) for country in countries}

print(population_v2)

###################################Convertir 2 listas a un solo diccionario
names=['nico', 'zule','santi']
ages=[12,56,98]

#Primero debemos unir las dos listas con la funcion ZIP
#ZIP solo crea una referencia y la tenemos que convertir a una lista

print(list(zip(names,ages)))

new_dictionary = {name:age for (name,age) in zip(names,ages)}
print(new_dictionary)