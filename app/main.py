import utils#Este es el modulo que nosotros creamos
import readCSV
import charts


def run():
    data = readCSV.readCSV('./app/data.csv') #Usando nuestro modulo readCSV para que nos de la data que tiene
    country = input('Type Country => ')
    result = utils.populationByCountry(data,country)
    if len(result)>0:
        country = result[0]
        labels,values = utils.getPopulation(country)
        charts.generateBarChart(labels,values)

#Este if nos ayuda a ejecutar el archivo directamente desde la terminal
if __name__ == '__main__':
    run()