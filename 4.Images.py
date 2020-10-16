from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("800x600")        #1st width 
root.configure(bg="purple")

def hello():
    print("Hello")

im = PhotoImage(file="pause.png")
im = im.subsample(15,15)

btn1 = Button(root, text="Click", bg="yellow", fg="green",font=("arial", 15, "bold"),
        activebackground="blue", anchor=N, activeforeground="white", width=400,height=100,
        cursor="star",bd=8, relief=SOLID, command=hello,
        image=im, compound=RIGHT)    #relief bd type sunken, ridge, solid etc
btn1.pack()

lab1 = Label(root, text="Hello ", width=200, height=100, anchor=N,bg="white",
        fg="black", font=("chiller", 35, "italic bold underline"), cursor = "watch",
        relief=RIDGE, bd=6, image=im, compound=BOTTOM )
lab1.pack()

root.mainloop()