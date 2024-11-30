''' 
#importanto el paquete que creamos, con sus funciones
from pkg.mod1 import func1,func2 
import pkg.mod1 from pkg.mod2 import func3,func4
##############################################

print(func1())

print(func2())

print(func3())

print(func4())
#############################################
'''

'''
import pkg
print(pkg.URL)

print(pkg.mod1.func1())
'''


#Ejercicio clase 30 curso python
from pkg.myFunctions import get_totals, calc_total

def get_total(orders):
  prices = get_totals(orders)
  totalPrice = calc_total(prices)
  return  totalPrice

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)


#Fin ejercicio clase 30 curso python