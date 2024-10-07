import random

# loop= True

# while loop:
#     number = random.randint(1,10)

#     print(f"the number is {number}")
#     if number % 2 == 0:
#         print("Heads")
#     else:
#         print("Tails")

#     continue_or_not = str(input("continue? Y/N: ")).lower

#     if continue_or_not != "n":
#         print("ok")
#         loop= True
#     else:
#         print("bye")
#         loop = False
        

# friends = ["ana","alex", "renan", "angela", "fabio"]


# random_select = random.choice(friends)

# print(random_select)

x = True

while x:
    hands = ["rock", "scissor", "paper"]

    radom_player_hand = random.choice(hands)

    radom_bot_hand = random.choice(hands)

    if radom_player_hand == "rock" and radom_bot_hand == "scissor":
        print(f"PLAYER:{radom_player_hand} VS BOT:{radom_bot_hand} : Player Win")
    elif radom_player_hand == "paper" and radom_bot_hand == "rock":
        print(f"PLAYER:{radom_player_hand} VS BOT:{radom_bot_hand} : Player Win")
    elif radom_player_hand == "scissor" and radom_bot_hand == "paper":
        print(f"PLAYER:{radom_player_hand} VS BOT:{radom_bot_hand} : Player Win")
    elif radom_player_hand == radom_bot_hand:
        print(f"PLAYER:{radom_player_hand} VS BOT:{radom_bot_hand} : TIE")
    else:
        print(f"PLAYER:{radom_player_hand} VS BOT:{radom_bot_hand} : BOT Win")

    continue_or_not = str(input("Do you want continue? Y/N :")).lower
    if continue_or_not == "n":
        x = False
