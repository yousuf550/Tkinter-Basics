from tkinter import *
root = Tk()
root.title("GUI")
root.geometry("600x400")
root.configure(bg="light green")

def ff():
    ET1.insert(0, "rahul")
    print(ss.get())
    ss.set("")
ss = StringVar()

ET1 = Entry(root, bg="yellow", bd=4,fg="brown", font=("arial",18, "bold" ),
        insertbackground="green", insertwidth=5, justify="center", relief=RIDGE,
        selectbackground="red",selectforeground="blue", 
        textvariable=ss)  #show="*"

ET1.pack()
ET1.focus_set()

bt1 = Button(root, text="Click", command=ff)
bt1.pack()
root.mainloop()