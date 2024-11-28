#Transformaremos esta lista de diccionarios a una lista de numeros
items = [
    {
        'prooduct': 'Camisa',
        'price': 100
    },
    {
        'prooduct': 'pantalones',
        'price': 300
    },
    {
        'prooduct': 'Shorts',
        'price': 300
    },
]

#Queremos tener una lista solo de los precios

prices = list(map(lambda item: item['price'], items))

print(prices)

#Agregando un atributo nuevo a un diccionario ya existente

def addTaxes(item):
    #Coping the inital array to another one, to not modify the original one
    newItem = item.copy()
    newItem['taxes'] = newItem['price'] * .19
    return newItem


newItems = list(map(addTaxes,items))

print(newItems)