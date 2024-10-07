# def calculate_love_score(name1,name2):
#     x = "love"
#     y = "true"
#     loveCount = 0
#     trueCount = 0
#     for _ in name1:
#         if _ in x:
#             loveCount += 1
#         if _ in y:
#             trueCount += 1
#     for _ in name2:
#         if _ in x:
#             loveCount += 1
#         if _ in y:
#             trueCount += 1
#     return print (f"{trueCount}{loveCount}")
    
# calculate_love_score("Angela Yu","Jack Bauer")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']




x = True
while x:
    text = str(input("type your mensage\n"))
    shift = int(input("type the shift number \n"))
    choice = str(input("Encode or decode\n"))
    
    def encode (textToCode , numberToCode):
        textEncrypted = ''
        for indexLetter in textToCode:
            searchWords = alphabet.index(indexLetter)+ numberToCode

            searchWords %= len(alphabet)
            textEncrypted += alphabet[searchWords]

        return textEncrypted

    def decode (textToCode , numberToCode):
        textEncrypted = ''
        for indexLetter in textToCode:
            searchWords = alphabet.index(indexLetter) - numberToCode

            searchWords %= len(alphabet)
            textEncrypted += alphabet[searchWords]

        return textEncrypted

    if choice == "decode":
        print(decode(text,shift))
    elif choice == "encode":
        print(encode(text,shift))
    else:
        print("finished")
    
    ask = str(input("continue? "))
    if ask != 'yes':
        print("finished")
        x = False
    else:
        x = True
            