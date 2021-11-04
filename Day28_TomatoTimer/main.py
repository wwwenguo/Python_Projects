from tkinter import *
import math

PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

window = Tk()
window.title('Pomodorg')
window.config(padx=100, pady=50, bg=YELLOW)


def start_count():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text='Break', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label.config(text='Work', fg=GREEN)


def reset():
    window.after_cancel(timer)
    label.config(text='Timer')
    canvas.itemconfig(canvas_text, text="00:00")
    check_mark.config(text='')
    global reps
    reps = 0


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        mark = ''
        for _ in range(math.floor(reps / 2)):
            mark += '√'
        check_mark.config(text=mark)


tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 35, 'bold'), bg=YELLOW, highlightthickness=0)
label.grid(row=0, column=1)

start_button = Button(text='Start', command=start_count)
start_button.grid(row=2, column=0)

Reset_button = Button(text='Reset', command=reset)
Reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, font=(FONT_NAME, 15, 'bold'), bg=YELLOW, highlightthickness=0)
check_mark.grid(row=3, column=1)

window.mainloop()
