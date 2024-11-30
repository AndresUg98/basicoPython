file = open('./text.txt')

#print(file.read()) leyendo todo el texto

#print(file.readline()) #leyendo linea por liena
#print(file.readline()) #leyendo linea por liena
#print(file.readline()) #leyendo linea por liena


for line in file: #leyendo linea por linea con un "for"
    print(line)




file.close() #Sirve para cerrar el archivo


with open('./text.txt') as file: #nos permite abir el archivo y este se cerrara automaticamente
    for line in file: #leyendo linea por linea con un "for"
     print(line)