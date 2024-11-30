import csv

def readCSV(path):
    with open(path,'r') as csvFile:
        reader = csv.reader(csvFile,delimiter=',')#reader es un iterable
        header = next(reader)
        data=[]
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
   data = readCSV('./app/data.csv')
   print(data[0])


