from prettytable import PrettyTable


table = PrettyTable()

table.add_column("Pokemon",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Eletric", "Water", "Fire"])

table.align = "l"

print(table)