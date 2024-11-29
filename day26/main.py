# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas


file = pandas.read_csv("day26/nato_phonetic_alphabet.csv")

def natoEncoding(name):
    name = [l.upper() for l in name]
    newName = [row.code for i in name for index,row in file.iterrows() if row.letter == i]
    print(newName) 
    

# natoEncoding("sergio")


def oldNatoEncoding(name):
    newName = []
    for l in name:
        l.upper()
        newName.append(l)
    print(newName)
    nameEncoded = []
    for i in newName:
        for index , row in file.iterrows():
            if row.letter == i:
                nameEncoded.append(row.code)
    print(nameEncoded)
    
oldNatoEncoding("sergio")