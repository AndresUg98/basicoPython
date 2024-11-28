#Creando el conjunto
set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
 #imprimiendo el tamaño del conjunto 
print(size)

#Preguntando si un elemento esta en un conjunto
print('col' in set_countries)
print('pe' in set_countries)


#Agregar mas elementos al conjunto
set_countries.add('pe')
print(set_countries)
#Revisando si podemos agregar el mismo elemento otra vez y duplicarlo, pero vemos que esto no es posible en los conjuntos
set_countries.add('pe')
print(set_countries)

#Actualizar un conjunto (update), funciona como "add" pero en "update" podemos añadir mas conjuntos
set_countries.update({'ar','ecua','pe'})
print(set_countries)

#eliminar elementos de un conjunto
set_countries.remove('col')
print(set_countries)

#eliminar elementos que no existe de un conjunto
# "Discard" al momento de no encontra un elemnto, no va a fallar commo si pasa en el caso de remove
set_countries.discard('arg')
print(set_countries)

#Limpiar o eliminar todo el conjunto
set_countries.clear()
print(set_countries)
