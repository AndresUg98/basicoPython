suma = lambda x,y : x + y
assert suma(2,2) == 4 #Assert asegura que el resultado sera 4, si no lo es arrojara un error

age = 10

if age < 18:
    raise Exception('No se permiten menores de edad') #lanzando nuestro propio error


#El programa se detendra cada que detecte un error