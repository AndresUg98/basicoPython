def sumWithRange(min, max):
    print(min, max)
    sum = 0

    for x in range (min,max):
        sum += x
    return sum

result = sumWithRange(1,10)

result2 = sumWithRange(result,result+10)

print(result)
print(result2)