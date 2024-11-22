

# import csv


# with open("day25/weatherDatas.txt") as file:

#     data = file.readlines()
#     for l in data:
#         print(l)


# file.close()

# with open("day25/weatherDatas.txt") as data_file:
#     x = csv.reader(data_file)
#     temperutes = []
#     for row in x:
#         if row[1] != "temp":
#             temperutes.append(int(row[1]))
##############################------------###################################
import pandas
data = pandas.read_csv("day25/weatherDatas.txt")

data_dict = data.to_dict()
# print(data_dict["day"])

# print(data[data.temp == data["temp"].max()])


data_dict = {
 "students": ["ana", "james", "lucas"],
 "score": [76,58,65]
}

newData = pandas.DataFrame(data_dict)
newData.to_csv("new_data.csv")

print(newData)