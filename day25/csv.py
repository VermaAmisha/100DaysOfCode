
# with open("weather_data.csv") as data_file:

#     data = data_file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []

    for row in data:
        # print(row[1])
        # by this way the whole column gets printed along with the label

        # to remove the label
        if row[1] != "temp":
            temperature.append(row[1])
    print(temperature)
