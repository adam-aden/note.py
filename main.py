import tkinter
tk = tkinter
root = tk.Tk()

read = tk.Label(root, text="hi welcome to note", width=100, height=5)
read.pack()

write = tk.Entry(root, width=100,)
write.pack()

ls = []
def show():
    text = write.get()
    print(text)
    ls.append(text)
    print(ls)
click = tk.Button(root, text= "click", width=40, command=show)
click.pack()



    
root.mainloop()