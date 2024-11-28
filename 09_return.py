#Functions with arguments by default
def findVolume(length = 2, width = 4, depth = 6):
    #returning multiple values
    return length * width * depth, width,"hola"


result = findVolume(5,4,6)
#sending just one value
#Creating variables for each index of the "tupla"
result2,width,text = findVolume(width=30) 


#Printing each declared variable
print(result)
print(result2)
print(width)
print(text)