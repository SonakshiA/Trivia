from tkinter import *
import json
import requests

def nextque():
    window.destroy()
    import q1

window = Tk()
window.geometry("900x350")
window.title("Trivia Game")
window.configure(bg="pink")
label = Label(window, text="TRIVIA GAME",bg="pink",font=("Times New Roman",30,"bold underline"))
label.pack()


Label(text="Welcome to Trivia Quiz!"
           "\n\nYou will face 10 questions."
           "\nYou get one attempt for each question."
           "\nFor every right answer, you get 1 point."
           "\nYour score will be displayed at the end."
      "\nYou get 10 seconds for each question.",bg="pink", font = ("Times New Roman",20)).pack(pady=20)

button = Button(window, text="Next", command=nextque, bg="AntiqueWhite2",font=("Times New Roman",20))
button.pack()

window.mainloop()