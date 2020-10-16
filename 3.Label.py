from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("800x600")        #1st width 
root.configure(bg="blue")

lab1 = Label(root, text="Hello world", width=20, height=5, anchor=N,bg="black",
        fg="white", font=("chiller", 35, "italic bold underline"), cursor = "watch",
        relief=RIDGE, bd=6 )
lab1.pack()
root.mainloop()