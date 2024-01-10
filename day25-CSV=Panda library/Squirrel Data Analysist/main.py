import pandas
# get the whole data
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"]== "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"]== "Red"])
black_squirrel_count = len(data[data["Primary Fur Color"]== "Black"])

data_dict={
    "Fur Color":["Gray", "Black", "Red"],
    "Count":[grey_squirrel_count, black_squirrel_count, red_squirrel_count]
}
data_dataFrame= pandas.DataFrame(data_dict)
data_dataFrame.to_csv("squirrel_count_color.csv")