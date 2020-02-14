import csv

data = []
with open('data/2019_nCoV_20200121_20200131.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        data.append(row)


countryData = []
for row in data:
    if row[1] in countryData:
        continue

    countryData.append(row)


