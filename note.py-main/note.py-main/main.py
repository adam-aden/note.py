import tkinter
tk = tkinter
root = tk.Tk()

read = tk.Label(root, text="hi welcome to note", width=100, height=5)
read.pack()

write = tk.Entry(root, width=100,)
write.pack()

click = tk.Button(root, text="click", width=40) 
click.pack()


def show(click, write):
    print(write.get())
click = tk.Button

root.mainloop()