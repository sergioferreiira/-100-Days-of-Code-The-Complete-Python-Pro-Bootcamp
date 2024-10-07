# travel_log = {
#     "France": ["paris", "lille", "dijon"],
#     "Germany" : [ "Stuttgart", "Berlin"]
# }

# nested_list = ["a","b",["c","d"]]

# travel_log2 = {
#     "France": {
#         "cities_visited": ["paris", "lille", "dijon"],
#         "total_visits": 12
#     },
#     "Germany": {
#         "cities_visited": [ "Berlin","Hamburg","Stuttgart"],
#         "total_visits": 12
#     }
# }

# print(travel_log2["Germany"]["cities_visited"][2])


print("Welcome to the secret auction program.\n")

z = True
auctions_biders = {}

while z:
    x = str(input("What is your name? \n"))
    y = int(input("How much ill bid? \n"))

    def bids(name , bid):
        auctions_biders[name] = bid

    bids(x,y)


    w = str(input("Someone more to bid? YES / NO \n"))
    if w != "no":
        z = True
    else:
        z = False

price = 0
for value in auctions_biders:
    if auctions_biders[value] > price:
        price = auctions_biders[value]

for value in auctions_biders:
    if auctions_biders[value] == price:
        print("the winner is ", value , " with " , auctions_biders[value])