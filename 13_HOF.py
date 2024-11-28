#Una función de Orden Superior o en sus siglas HOF se le lama así solo cuando 
#contiene otras funciones como parámetro de entrada o devuelve una función como salida

def increment(x):
    return x + 1

incrementV2 = lambda x: x+1

def highOrderFunciton(x,func):
    return x + func(x)

highOrderFuncitonV2 = lambda x,func: x + func(x)

result = highOrderFunciton(2,increment)

result2 = highOrderFuncitonV2(2,incrementV2)

print(result)
print(result2)