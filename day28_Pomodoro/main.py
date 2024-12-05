from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
pauseCounter = 1


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def startCountDown():
   global pauseCounter
   if pauseCounter == 1 or pauseCounter == 3 or pauseCounter == 5 or pauseCounter == 7:
      countDown(WORK_MIN * 60)
      print(f"timer {pauseCounter}")
   elif pauseCounter == 2 or pauseCounter == 4 or pauseCounter == 6:
      countDown(SHORT_BREAK_MIN * 60)
      print(f"pause {pauseCounter}")
   elif pauseCounter == 8:
      countDown(LONG_BREAK_MIN * 60)
      print(f"pause long{pauseCounter}")
   else:
      canvas.itemconfig(timer_text,text=f"FIM")
      print(pauseCounter)


# def startShortBreak():
#    shortPauseCountDown(SHORT_BREAK_MIN * 60)
   
# def startLongBreak():
#    longPauseCountDown(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
   global pauseCounter

   count_min = math.floor(count / 60)
   count_sec = count % 60
   canvas.itemconfig(timer_text,text=f"{count_min:02}:{count_sec:02}")

   if count > 0:
      window.after(1,countDown,count -1)
   if count == 0:
      pauseCounter += 1
      startCountDown()


# def shortPauseCountDown(count):
#    moment.config(text="Pause")
#    global pauseCounter
#    count_min = math.floor(count / 60)
#    count_sec = count % 60

#    canvas.itemconfig(timer_text,text=f"{count_min:02}:{count_sec:02}")
#    if count > 0:
#       window.after(5,shortPauseCountDown,count -1)
#    if count == 0:
#       if pauseCounter == 4:
#          startLongBreak()
#       else:
#          pauseCounter +=1
#          print(pauseCounter)
#          startCountDown()

# def longPauseCountDown(count):
#    moment.config(text="Long Pause")
#    global pauseCounter
#    count_min = math.floor(count / 60)
#    count_sec = count % 60

#    canvas.itemconfig(timer_text,text=f"{count_min:02}:{count_sec:02}")
#    if count > 0:
#       window.after(5,longPauseCountDown,count -1)

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


timer_text = canvas.create_text(100,130,text=f"00:00",fill="white",font=(FONT_NAME,30,"bold"))


startButton = Button(text="Start", command=startCountDown)
startButton.grid(row=2, column=0)

emoji = "✔️"
emojilabel = Label(text=emoji, font=(10), fg="green", bg=YELLOW)
emojilabel.grid(row=3, column=1)


resetButton = Button(text="Reset")
resetButton.grid(row=2, column=2)





window.mainloop()

