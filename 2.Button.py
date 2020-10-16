from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("800x600")        #1st width 
root.configure(bg="purple")

def hello():
    print("Hello")

btn1 = Button(root, text="Click", bg="yellow", fg="green",font=("arial", 15, "bold"),
        activebackground="blue", activeforeground="white", width=20,height=2,
        cursor="star", anchor=NE,
        bd=8, relief=SOLID, command=hello)    #relief bd type sunken, ridge, solid etc
btn1.pack()



root.mainloop()