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
    item['taxes'] = item['price'] * .19
    return item


newItems = list(map(addTaxes,items))

print(newItems)