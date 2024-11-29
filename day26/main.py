import pandas as pd

x = pd.read_csv("day26/natoAlpab.csv")

def encodingNato(name):
 name = [l.upper() for l in name]
 newNameEncoded = [row.code for i in name for index, row in x.iterrows() if row.letter == i]
 print(newNameEncoded)


encodingNato("sergio")