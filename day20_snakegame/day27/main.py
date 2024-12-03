from tkinter import *


window = Tk()
window.title("My first windown using tkinter")
window.minsize(800,600)




my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


def clickbutton():
    my_label.config(text=f"{input.get()}", font=("Arial", 24, "bold"))


input = Entry()
input.pack()


button = Button(text="click me", command= clickbutton)
button.pack()














window.mainloop()