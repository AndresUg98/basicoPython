numbers = [1,2,3,4,5,6]


newNumbers = list(filter(lambda number : number % 2 == 0, numbers))

print(newNumbers)