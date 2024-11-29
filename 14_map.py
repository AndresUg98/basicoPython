numbers = [1,2,3,4]
numbersV2 = [5,6,7]

#Map primero recibe una lambda que nos dice que va a hacer map, y despues de la "," pondremos los arrays que usaremos

newNumbers = list(map(lambda number: number * 2, numbers))

newNumbersV2 = list(map(lambda x, y : x + y, numbers, numbersV2))

print(newNumbers)
print(newNumbersV2)


#Para resolver este desafío, tu reto es utilizar la función map de Python y una función lambda para transformar una lista de números. 
#Debes retornar una lista en la que cada número de la lista original sea multiplicado por dos.
#La función multiply_numbers recibirá como entrada una lista con números. Finalmente, la función retornará la lista transformada.

def multiply_numbers(numbers):
    answer = list(map(lambda number: number * 2, numbers))
    return answer

numbers = [1, 1, -2, -3]

response = multiply_numbers(numbers)
print(response)