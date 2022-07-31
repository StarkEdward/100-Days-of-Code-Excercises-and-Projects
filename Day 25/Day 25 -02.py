import pandas

# data = pandas.read_csv("weather-data.csv")
# print(type(data))
# print(data["temp"])

# convert csv to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# convert to list
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# # printin average temperature
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# or
# print(data["temp"].mean())
# get maximum value form temp using pandas
# print(data["temp"].max())


# Get Data in Column
# print(data["condition"])
# alternate way to display
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max() ])


# monday = data[data.day == "Monday"]
# print(monday.condition)

# temp convert degree to F
# monday_temp = int(monday.temp)
# monday_temp_f =  monday_temp * 9/5 + 32
# print(monday_temp_f)


# Creat a datafram from scratch

data_dict = {
    "students" : ["Amy", "James", "Edward"],
    "scores" : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")