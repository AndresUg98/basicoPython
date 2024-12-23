
import matplotlib.pyplot as plt #libreria para hacer graficas, recuerda que esta se debe instalar

#Funcion para generar grafica

def generateBarChart(labels, values):

    fig,ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generatePieChart(labels, values):
    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':

    labels = ['a', 'b', 'c']
    values = [100,800,80]
    generateBarChart(labels, values)
    generatePieChart(labels, values)