with open('./text.txt','w+') as file: #nos permite abir el archivo y este se cerrara automaticamente, con permisos de escritura y lectura
    for line in file: #leyendo linea por linea con un "for"
     print(line)
    file.write('Nuevas cosas en este archivo\n') #Escribiendo en el archivo
    file.write('Nuevas cosas en este archivo\n')
    file.write('Nuevas cosas en este archivo\n')

    #"w+" lee el archivo y reemplaza todo lo que esta en el archivo
    #por las nuevas lineas que estas escibiendo