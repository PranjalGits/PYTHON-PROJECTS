from textblob import TextBlob
from tkinter import *

def correct_spelling():
    get_data = entry1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    entry2.delete(0,END)
    entry2.insert(0,data)



def main_win():
    global  entry1,entry2
    win = Tk()
    win.geometry("500x370")
    win.resizable(False,False)
    win.config(bg="Blue")
    win.title("spelling checker")

    label1 = Label(win,text = "Incorrect spelling",font=("time new Roman",25,"bold"),bg = "blue",fg = "white")
    label1.place(x=100,y=20,height=50,width=300)

    entry1 = Entry(win,font=("time new Roman",20))
    entry1.place(x=20,y=80,height=50,width=400)

    label2 = Label(win, text="Correct spelling", font=("time new Roman", 25, "bold"), bg="blue", fg="white")
    label2.place(x=100, y=140, height=50, width=300)

    entry2 = Entry(win, font=("time new Roman", 20))
    entry2.place(x=20, y=200, height=50, width=400)

    button = Button(win,text=("DONE"),font=("time new Roman", 25, "bold"), bg="yellow",command=correct_spelling)
    button.place(x=150,y=280,height=50,width=200)

    win.mainloop()

main_win()