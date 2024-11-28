price = 100 #Variable in the global scope, it can be used by other functions

def increment():
    # Local Scope: a varibel will only work in their block of code
    # It doesn't matter if the variables have the same name, as long they are in different scopes. Because of the context
    price = 200
    result = price + 10
    return(result)

print(price)
price2 = increment()
print(price2)

#print(result)#This will throw an error, "result" just exist in the funciton "increment"