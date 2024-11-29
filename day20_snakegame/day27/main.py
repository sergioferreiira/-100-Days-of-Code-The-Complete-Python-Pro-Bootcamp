import tkinter


window = tkinter.Tk()
window.title("My first windown using tkinter")
window.minsize(800,600)




my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)

















window.mainloop()