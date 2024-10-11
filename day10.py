import random

def playGame (play):
    def drawTwoCards (x=list):
        x.append(random.choice(cards))
        x.append(random.choice(cards))
    
    def drawAnotherCard(x=list):
        x.append(random.choice(cards)) 

    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    player_hand = []
    computer_hand = []

    while play:
        
        drawQuestion = True

        drawTwoCards(player_hand)
        drawTwoCards(computer_hand)


        print(f"player numbers : {player_hand}, Sum : {sum(player_hand)}")   
        print(f"Computer numbers : {computer_hand[0]}")   


        question = str(input("type 'y' to get another card, type 'n' to pass:\n"))
        if question.lower() == "y":
            while drawQuestion:
                    drawAnotherCard(player_hand)
                    if sum(player_hand) > 21:
                        print("You lose")
                        print(f"player numbers : {player_hand}, Sum : {sum(player_hand)}")   
                        print(f"Computer numbers : {computer_hand}, Sum : {sum(computer_hand[0])}")  
                        play = False
                    
                    newQuestion = str(input("type 'y' to get another card, type 'n' to pass:\n"))
                    if newQuestion.lower() != "y":
                        drawQuestion = False

        if sum(player_hand) > sum(computer_hand) and sum(player_hand)<= 21:
            print("Player win")
            print(f"player numbers : {player_hand}, Sum : {sum(player_hand)}")   
            print(f"Computer numbers : {computer_hand}, Sum : {sum(computer_hand)}") 
            play = False 
        elif sum(computer_hand) > sum(player_hand) and sum(player_hand)<= 21:
            print("Computer win")
            print(f"player numbers : {player_hand}, Sum : {sum(player_hand)}")   
            print(f"Computer numbers : {computer_hand}, Sum : {sum(computer_hand)}")  
            play = False
    


wanna_play = str(input("Welcome to the blackjack Cassino online \n Do you want to play? y / n \n"))

if wanna_play.lower() != "y":
    print("bye")
else:
    playGame(True)


        


    

