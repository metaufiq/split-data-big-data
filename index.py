import csv
import copy
data = []
line = 0
with open('data/2019_nCoV_20200121_20200131.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        if line == 0:
            line+=1
            continue
        data.append(row)


countryData = []
for row in data:
    if row[1] in countryData:
        continue
    
    converter1 = copy.deepcopy(row)
    
    countryData.append(row[1])
    converter1[1] = countryData.index(row[1])
    with open('./output/output1.csv', mode='a+',newline='') as employee_file:
        csv_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(converter1)    
    with open('./output/output2.csv', mode='a+',newline='') as employee_file:
        csv_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([countryData.index(row[1]), row[1]])


