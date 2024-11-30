import functools #importando "reduce"

numbers = [1,2,3,4]

def accum(counter,item):
    print(counter)
    print(item)
    return counter + item

result = functools.reduce(lambda counter, item : counter + item,numbers)
result2 = functools.reduce(accum,numbers)
print(result)
print(result2)
