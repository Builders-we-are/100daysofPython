from statistics import *
import pandas
import csv
import os

os.system("clear")

with open("./weather_data.csv")as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(row[1])
# print(temp)


data = pandas.read_csv("weather_data.csv")

# print(type(data.loc[4].to_list))
# print((data.loc[4].to_list.item()))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

# print(mean(temp_list))

# print(data["temp"].max())

# print(data[data.day == "Monday"])

# print(data[data.temp == max(data["temp"])])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp[0])
# print(monday_temp*9/5+32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")
