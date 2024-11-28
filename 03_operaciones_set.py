set_a = {'col', 'mex', 'bol'}

set_b = {'pe', 'bol'}

#Uniendo conjuntos con el metodo "union", no duplicara los elementos
set_c = set_a.union(set_b)
print(set_c)

#Uniendo conjuntos con operadores "|", no duplicara los elemntos
print(set_a | set_b)

#Revisando cuales son los elementos que tienen en comun los conjuntos, con metodo
set_c = set_a.intersection(set_b)
print(set_c)

#Revisando cuales son los elementos que tienen en comun los conjuntos, con operadores
print(set_a&set_b)

#Revisando cuales son los elementos que tienen diferentes los conjuntos, con metodos
set_c = set_a.difference(set_b)
print(set_c)

#Revisando cuales son los elementos que tienen diferentes los conjuntos, con operadores
print(set_a-set_b)


#Diferencia simetrica, se hara una union excluyendo a los elementos en comun (La interseccion de los conjuntos), con metodo
set_c = set_a.symmetric_difference(set_b)
print(set_c)

#Diferencia simetrica, se hara una union excluyendo a los elementos en comun (La interseccion de los conjuntos), con operador
print(set_a ^ set_b)

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries | northAm |centralAm | southAm


print(new_set)