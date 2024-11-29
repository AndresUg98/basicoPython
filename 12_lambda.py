def increment(num):
    return num + 1

#Es una funcion con sintaxis mas corta
incrementV2=lambda num : num + 1

result = increment(3)
result2 = incrementV2(20)

print(result)
print(result2)

fullName = lambda name,lastName : f'Full name is {name.title()} {lastName.title()}'

text = fullName("andres","ugarte")

print(text)


