#build gui
import tkinter
tk = tkinter
root = tk.Tk()
#build widget
read = tk.Label(root, text="welcome to note", width=100, height=5)
read.pack()

write = tk.Entry(root, width=100,)
write.pack()

show_list = tk.Listbox(root, width=100, height=20)
show_list.place(x = 380, y = 150)

old_file = open("note.txt", "r")
content = old_file.read()
lines = content.split("\n")
for line in lines:
    show_list.insert("end", line)
old_file.close()
print(content)

ls = []

def show():
    text = write.get()
    print(text)
    ls.append(text)
    print(ls)
    print(content)
    f = open("note.txt", "a")
    f.write(text + "\n")
    f.close()
    show_list.insert("end", text)

def delete_note():
    selected = show_list.curselection()
    print(selected)
click = tk.Button(root, text= "click", width=10, command=show)
click.place(x = 902, y = 100)

delete_btn = tk.Button(root, text = "delete", width = 10, command=delete_note)
delete_btn.place(x = 902, y = 125)

    
root.mainloop()