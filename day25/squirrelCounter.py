import pandas

squirrelData = pandas.read_csv("day25/squirrelData.csv")

contagens = squirrelData['Primary Fur Color'].value_counts()

print(contagens)

saveToCsv = pandas.DataFrame(contagens).to_csv("SquirrelConts.csv")

