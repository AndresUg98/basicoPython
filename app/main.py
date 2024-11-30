import utils#Este es el modulo que nosotros creamos

data=[
    {
        'Country':'Colombia',
        'Population':300
    },
    {
        'Country':'Mexico',
        'Population':200
    },
]

def run():

    keys,values = utils.getPopulation()
    print(keys,values)




    country = input('Type the country =>')

    result = utils.populationByCountry(data,country)
    print(result)

#Este if nos ayuda a ejecutar el archivo directamente desde la terminal
if __name__ == '__main__':
    run()