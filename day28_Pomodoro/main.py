from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
second = 00
minute = 25

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def clickStart ():
 START_POMODORO = True
 second = 59
 minute = 25
 while START_POMODORO:
  while minute != 0:
   while second != 0:
    second -=1
    time.sleep(1)
   minute -=1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 



  

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.minsize(width=300,height=300)
window.config(bg=YELLOW, padx=40,pady=40)

moment = Label(text="Timer", background=YELLOW,font=(FONT_NAME,35,"bold"))
moment.grid(row=0,column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="day28_Pomodoro\Tomato.png")
canvas.create_image(100,112,image =tomatoImg)
canvas.grid(row=1,column=1)


canvas.create_text(100,130,text=f"{minute:02}:{second:02}",fill="white",font=(FONT_NAME,30,"bold"))


startButton = Button(text="Start", command=clickStart)
startButton.grid(row=2, column=0)

emoji = "✔️"
emojilabel = Label(text=emoji, font=(10), fg="green", bg=YELLOW)
emojilabel.grid(row=3, column=1)


resetButton = Button(text="Reset")
resetButton.grid(row=2, column=2)





window.mainloop()

