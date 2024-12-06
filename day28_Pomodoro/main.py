from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
pauseCounter = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def restCountDown():
   global pauseCounter
   pauseCounter = 0
   canvas.itemconfig(timer_text, text="25:00")
   moment.config(text="Timer")
   emojilabel.config(text="✔️" * pauseCounter, padx=0, pady=0)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def startCountDown():
   global pauseCounter

   if pauseCounter == 0 or pauseCounter == 2 or pauseCounter == 4 or pauseCounter == 6:
      moment.config(text="Timer", fg="green")
      countDown(WORK_MIN * 60)
   elif pauseCounter == 1 or pauseCounter == 3 or pauseCounter == 5:
      moment.config(text="Pause", fg="pink")
      countDown(SHORT_BREAK_MIN * 60)
   elif pauseCounter == 7:
      moment.config(text="Pause", fg="pink")
      countDown(LONG_BREAK_MIN * 60)
   else:
      moment.config(text="End")
      print(pauseCounter)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
   global pauseCounter

   count_min = math.floor(count / 60)
   count_sec = count % 60
   canvas.itemconfig(timer_text,text=f"{count_min:02}:{count_sec:02}")

   if count > 0:
      window.after(1000,countDown,count -1)
   if count == 0:
      pauseCounter += 1
      emojilabel.config(text="✔️" * pauseCounter, padx=0, pady=0)
      startCountDown()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.minsize(width=300,height=300)
window.config(bg=YELLOW, padx=40,pady=40)

moment = Label(text="Timer", background=YELLOW,font=(FONT_NAME,35,"bold"))
moment.grid(row=0,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="day28_Pomodoro\\tomato.png")
canvas.create_image(100,112,image =tomatoImg)
canvas.grid(row=1,column=1)

timer_text = canvas.create_text(100,130,text=f"25:00",fill="white",font=(FONT_NAME,30,"bold"))

startButton = Button(text="Start", command=startCountDown)
startButton.grid(row=2, column=0)

emojilabel = Label( fg="green", bg=YELLOW)
emojilabel.grid(row=3, column=1)

resetButton = Button(text="Reset", command=restCountDown)
resetButton.grid(row=2, column=2)




window.mainloop()