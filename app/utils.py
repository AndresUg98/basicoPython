#Creando nuestro propio modulo

def getPopulation():
    keys= ['Col','Bol']
    values= [300,400]

    return keys,values


#Esta funcion recibe una lista que contiene diccionarios "data"

def populationByCountry(data,country):
    result = list(filter(lambda item : item['Country']== country,data))
    return result
