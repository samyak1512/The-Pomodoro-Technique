from tkinter import *
import math
from winsound import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
paused = 'false'
paused_on_sec = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label_timer.config(text='Timer', fg=GREEN)
    reps = 1
def pause_timer():
    global paused
    window.after_cancel(timer)
    paused = 'true'

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global paused
    if paused == 'true':
        paused = 'false'
        count_down(paused_on_sec)
    else:

        global reps

        work_sec = WORK_MIN*60
        short_break_sec = SHORT_BREAK_MIN*60
        long_break_sec = LONG_BREAK_MIN*60

        if reps==1 or reps==3 or reps==5 or reps==7:
            count_down(work_sec)
            label_timer.config(text='Study', fg=GREEN)
        if reps == 2 or reps == 4 or reps == 6 :
            count_down(short_break_sec)
            label_timer.config(text='Break', fg=PINK)
        if reps == 8:
            count_down(long_break_sec)
            label_timer.config(text='Break', fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global paused_on_sec
    count_min = math.floor(count/60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f'0{count_sec}'


    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count-1)
        paused_on_sec = count
    if count == 0 :
        reps += 1
        PlaySound("Blop.wav", SND_FILENAME)
        if reps < 9:
            start_timer()
            if reps % 2 == 0:
                checks = math.floor(reps/2)*('✔')
                label_checkbox.config(text=f'{checks}')



# ---------------------------- UI SETUP ------------------------------- ✔#

window = Tk()
window.title('Pomodor')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 105, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)



label_timer = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
label_timer.grid(row=0, column=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(row=2, column=2)

pause_button = Button(text='Pause', command=pause_timer)
pause_button.grid(row=2, column=1)

label_checkbox = Label(fg=GREEN, bg=YELLOW)
label_checkbox.grid(row=3, column=1)









window.mainloop()