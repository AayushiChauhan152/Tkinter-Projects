from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")


def time():
    tym = strftime('%H:%M:%S  %p')
    lbl.config(text=tym)
    lbl.after(1000, time)


lbl = Label(root, font=('Calibri', 40), fg='white', bg='gray')
lbl.pack(anchor='center')

time()
root.mainloop()
