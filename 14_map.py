numbers = [1,2,3,4]
numbersV2 = [5,6,7]

#Map primero recibe una lambda que nos dice que va a hacer map, y despues de la "," pondremos los arrays que usaremos

newNumbers = list(map(lambda number: number * 2, numbers))

newNumbersV2 = list(map(lambda x, y : x + y, numbers, numbersV2))

print(newNumbers)
print(newNumbersV2)

