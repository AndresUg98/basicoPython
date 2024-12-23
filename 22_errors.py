#La excepcion "Try" nos permite escribir bloques de codigo que
#pueden tener errores y que cuando ocurran estos que 
# el codigo no se para en seco
try:
    print(0/0)
    assert 1 != 1, 'Uno no es igual que uno'
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)

#De esta forma podemos poner varios tipos de error de
#forma independiente, se detendran las instrucciones del mismo
#bloque, atrapando solo el primer error que aparezca



    
print('Hola')

#Para resolver este desafío, debes utilizar la función my_divide, 
#que recibe dos parámetros de entrada que representan los números 
#a dividir. Dentro de esta función, debes implementar la lógica 
#necesaria para capturar la excepción ZeroDivisionError. 
#También, debes retornar un mensaje que diga No se puede dividir 
#por 0 cuando esta excepción ocurra.

def my_divide(a, b):
   try:
      result = a / b 
   except ZeroDivisionError as error:
     result = "No se puede dividir por 0"
   return result


    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0