from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.download()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)



sp = Tk()
sp.title("Internet speed Test")
sp.geometry("500x700")
sp.config(bg = "Blue")
lab = Label(sp,text = "Internet speed test", font=("Time New Roman",30,"bold" ),bg = "blue", fg = "White")
lab.place(x=55,y=40,height=50,width=380)

lab = Label(sp,text = "Download speed", font=("Time New Roman",30,"bold" ))
lab.place(x=55,y=130,height=50,width=380)

lab_down = Label(sp,text = "00", font=("Time New Roman",30,"bold" ))
lab_down.place(x=55,y=200,height=50,width=380)

lab = Label(sp,text = "Upload speed", font=("Time New Roman",30,"bold" ))
lab.place(x=55,y=290,height=50,width=380)

lab_up = Label(sp,text = "00", font=("Time New Roman",30,"bold" ))
lab_up.place(x=55,y=360,height=50,width=380)

button = Button(sp,text = "Check Speed",font = ("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command=speedcheck)
button.place(x=55,y=460,height=50,width=380)


sp.mainloop()
