import random

print("Welcome to hangman! \n lets start")

words = ["apple", "banana", "challenge", "sky", "success", "code"]
guesses = []
game = True
chances = 6

random_word= list(random.choice(words))
word = []

for _ in random_word:
    word.extend("_")

print(f"The word is...{word}")
while game:
    count = 0

    letter_guess = str(input("Wanna guess a word? "))
    if letter_guess in guesses:
        print("you already wrote this letter")
    else:
        guesses.extend(letter_guess)

    for letter_in_word in random_word:
        if letter_guess == letter_in_word:
            word[count] = letter_guess
        count += 1
    
    if letter_guess not in random_word:
        chances -= 1
        if chances == 0:
            print("Game over")
            print(f"The correct answer was {''.join(random_word)}")
            break


    if word == random_word:
        print("finish very nice")
        game = False

    print(word)
