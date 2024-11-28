numbers = []

for element in range(1,11):
    numbers.append(element*2)

print(numbers)

##USANDO LIST COMPREHENSION
numbers_v2=[element*2 for element in range(1,11)]

print(numbers_v2)

##Añadiendo condicionales

numbers = []

for element in range(1,11):
    if element % 2== 0:
        numbers.append(element*2)

print(numbers)

##Añadiendo condicionales CON LIST COMPREHENSION

numbers_v2 = [element * 2 for element in range(1,11) if element%2==0]
print(numbers_v2)


numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [element for element in numbers if element % 2 == 0 ]

print('v2 =>', even_numbers_v2)