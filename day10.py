import random

space3 = print("\n" * 3)

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

space3
wanna_play = str(input("Welcome to the blackjack Cassino online \n Do you want to play? y / n \n"))

if wanna_play.lower() != "y":
    print("bye")

game = True

while game:
    def drawTwoCards (x=list):
        x.append(random.choice(cards))
        x.append(random.choice(cards))
    
    def drawAnotherCard(x=list):
        x.append(random.choice(cards)) 
    
    def print_cards_playerHands(x,y):
        print(f"Your cards : {x}, current score: {sum(y)}")

    def print_cards_computerHands(x,y):
        print(f"Your cards : {x}, current score: {sum(y)}")

    drawQuestion = True
    show_player_hand = print_cards_playerHands(player_hand,sum(player_hand))
    show_computer_hand = print_cards_computerHands(computer_hand,sum(computer_hand))

    player_hand = []
    computer_hand = []

    drawTwoCards(player_hand)
    drawTwoCards(computer_hand)

    show_player_hand
    show_computer_hand



    question = str(input("type 'y' to get another card, type 'n' to pass:\n"))
    if question.lower() == "y":
        while drawQuestion:
                drawAnotherCard(player_hand)
                if sum(player_hand) > 21:
                    print("You lose")
                    show_player_hand
                    show_computer_hand
                print(print_cards_playerHands)
                newQuestion = str(input("type 'y' to get another card, type 'n' to pass:\n"))
                if newQuestion.lower() != "y":
                    drawQuestion = False

    if sum(player_hand) > sum(computer_hand) and sum(player_hand)<= 21:
         print("Player win")
         print_cards_playerHands
         print_cards_computerHands
    elif sum(computer_hand) > sum(player_hand) and sum(player_hand)<= 21:
         print("Computer win")
         print_cards_playerHands
         print_cards_computerHands

        


    input(" ")

