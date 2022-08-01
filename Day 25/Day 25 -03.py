import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)

red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels_count)

black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)


# constructing a data frame

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrels_count.csv")