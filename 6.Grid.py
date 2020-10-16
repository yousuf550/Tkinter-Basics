from tkinter import *
root = Tk()
root.geometry("800x400")

# btn2 = Button(root, text="click", width=10, height=2, bg="red")
# btn2.grid(row=0, column=0)

# btn2 = Button(root, text="click", width=10, height=2, bg="red")
# btn2.grid(row=0, column=1)

# btn2 = Button(root, text="click", width=10, height=2, bg="red")
# btn2.grid(row=0, column=2)

# btn2 = Button(root, text="click", width=10, height=2, bg="red")
# btn2.grid(row=0, column=3)

# btn2 = Button(root, text="click", width=20, height=2, bg="red")
# btn2.grid(row=1, column=3, columnspan=2)

# btn2 = Button(root, text="click", width=20, height=2, bg="red")
# btn2.grid(row=2, column=3, columnspan=2)

# btn2 = Button(root, text="click", width=10, height=4, bg="red")
# btn2.grid(row=1, column=0, rowspan=2)

btn2 = Button(root, text="click", width=10, height=2, bg="red")
btn2.grid(row=0, column=0, ipadx=56, ipady=50, padx=50, pady=20)

btn2 = Button(root, text="click", width=10, height=2, bg="red")
btn2.grid(row=0, column=1, ipadx=56, ipady=50, padx=50, pady=20, sticky=N)



root.mainloop()