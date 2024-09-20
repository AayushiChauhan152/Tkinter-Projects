from tkinter import *
from textblob import TextBlob

root = Tk()
root.configure(background='skyblue')


def submit():
    word = input_.get()
    blob_obj = TextBlob(word)
    output_.insert(0, str(blob_obj.correct()))


def allClear():
    input_.delete(0, END)
    output_.delete(0, END)


titl = Label(root, text="Spell Corrector Application", font=(
    'calibari', 25), bg='gray', fg='white').grid(row=0, column=1, padx=10)
input_label = Label(root, text="Input Word")
input_label.grid(row=1, column=0, pady=20)
input_ = Entry(root, width=30)
input_.grid(row=1, column=1, pady=20)

btn = Button(root, text="Correction", command=submit).grid(
    row=2, column=1, columnspan=2, pady=10)

output_label = Label(root, text="Correct Word")
output_label.grid(row=3, column=0, padx=20)
output_ = Entry(root, width=30)
output_.grid(row=3, column=1, padx=20)

btn = Button(root, text="Clear", command=allClear).grid(
    row=4, column=1, columnspan=2, pady=10)


root.mainloop()
