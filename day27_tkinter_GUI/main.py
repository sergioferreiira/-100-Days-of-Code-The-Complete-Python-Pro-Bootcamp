from tkinter import *

def clickbutton():
    my_label.config(input.get(), font=("Arial", 24, "bold"))

window = Tk()
window.title("My first windown using tkinter")
window.minsize(800,600)




my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)


button = Button(text="click me", command= clickbutton)
button.grid(column=1,row=1)


input = Entry()
input.grid(column=3,row=0)

















window.mainloop()