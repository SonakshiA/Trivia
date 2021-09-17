import requests
import json
from tkinter import *
import random
import html  # to decode html entities like (&quot;, &pound;)
from API import dict
from q6 import score
import time

def sel():
    global score
    chosen = var.get()
    if (chosen == dict['results'][6]['correct_answer']):
        score += 1
        score_label.config(text=score)
    window.destroy()
    import q8

def countdown():
    times = int(sec.get())
    while times > -1:
        seconds = times % 60
        sec.set(seconds)
        window.update()
        time.sleep(1)
        if (times == 0):
            window.destroy()
            import q8
        times -= 1

window = Tk()
window.geometry("900x350")
window.configure(bg="pink")
window.title("Q7")
sec = StringVar()
Entry(window,textvariable=sec,width=2,bg="pink").pack(anchor="ne")
sec.set("10")
label = Label(window, text="TRIVIA GAME", bg="pink", font=("Times New Roman", 30, "bold underline"))
label.pack()

category = Label(window, text=dict['results'][6]['category'], bg="pink",
                 font=("Lucida", 17))
category.pack(pady=20)

Label(window, text="Q7.",bg="pink",font = ("Lucida",14,"bold")).pack(anchor="w")

question = Label(window, text=html.unescape(dict['results'][6]['question']), bg="pink", font=("Lucida", 14, "bold"))
question.pack(anchor="w")

num = random.randint(0, 3)
dict['results'][6]['incorrect_answers'].insert(num, dict['results'][6]['correct_answer'])

var = StringVar()

opt1 = Radiobutton(window, text=html.unescape(dict['results'][6]['incorrect_answers'][0]),
                   value=dict['results'][6]['incorrect_answers'][0], variable=var, command=sel, bg="pink")
opt1.pack(anchor="w")

opt2 = Radiobutton(window, text=html.unescape(dict['results'][6]['incorrect_answers'][1]),
                   value=dict['results'][6]['incorrect_answers'][1], variable=var, command=sel, bg="pink")
opt2.pack(anchor="w")

opt3 = Radiobutton(window, text=html.unescape(dict['results'][6]['incorrect_answers'][2]),
                   value=dict['results'][6]['incorrect_answers'][2], variable=var, command=sel, bg="pink")
opt3.pack(anchor="w")

opt4 = Radiobutton(window, text=html.unescape(dict['results'][6]['incorrect_answers'][3]),
                   value=dict['results'][6]['incorrect_answers'][3], variable=var, command=sel, bg="pink")
opt4.pack(anchor="w")

score_label = Label(window, text=score, bg="AntiqueWhite2",font=("Times New Roman",20))
score_label.pack()

countdown()

window.mainloop()


