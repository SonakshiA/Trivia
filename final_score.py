from tkinter import *
from q10 import score

window = Tk()
window.geometry("900x350")
window.configure(bg="AntiqueWhite2")

label = Label(window, text="Your score out of 10 is", bg="AntiqueWhite2", font=("Times New Roman",35,"bold"))
label.pack()
label = Label(window,text=score, bg="AntiqueWhite2", font=("Times New Roman",40,"bold"))
label.pack()

window.mainloop()