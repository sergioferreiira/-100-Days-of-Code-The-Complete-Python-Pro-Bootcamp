from tkinter import *
from input_checks import mileValues


def mileValues():
 mileValue = int(milesText.get())
 kmText.config(text=round(mileValue * 1.609))

window = Tk()
window.minsize(width=300, height=100)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

isEqualLabel = Label(text="is equal to")
isEqualLabel.grid(row=1,column=0)

milesText = Entry(width=10)
milesText.grid(row=0, column=1)

milesLabel = Label(text="Miles")
milesLabel.grid(row=0,column=2)


kmText = Label(width=10)
kmText.grid(row=1, column=1)

kmLabel = Label(text="Km")
kmLabel.grid(row=1,column=2)

calculateButton = Button(text="Calculate")
calculateButton.grid(row=2,column=2)
calculateButton.config(command= mileValues)



































window.mainloop()