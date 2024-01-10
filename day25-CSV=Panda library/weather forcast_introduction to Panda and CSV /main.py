# INTRODUCTION TO PANDA LIBRARY AND CSV FILE


# normal way
# with open('weather_data.csv') as data:
#     dataline=data.readlines()
#     print(dataline)

# 2.way: using csv library
# import csv
# with open("weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     for row in data:
#        print(row)
#     # print all the temperature from file

# 3way: using Panda library
import pandas
# data frame type, the whole tabelle
data=pandas.read_csv("weather_data.csv")
print(data)
# series type in pandas, kinda a list
temp=(data["temp"])
print(temp[1])
data_dict =data.to_dict()
print(data_dict)

temp_list= temp.to_list()
print(temp_list)

# calculate the whole average of week
avg_temp= temp.mean()
print(avg_temp)
# get the max of temp
data["temp"].max()
# get data in column
data["condition"]
print(data.condition)

# get data from row
monday=data[data.day =="Monday"]
# get the row with max temperature
print(data[data.temp==data.temp.max()])
# change the temp on monday to F
monday_temp= monday.temp[0]

# create csv from scratch
data_dict= {
    "student":["amy", "bell","co"],
    "scores":[75,54, 65]
}
data_dataframe =pandas.DataFrame(data_dict)
data_dataframe.to_csv("new_data.csv")
