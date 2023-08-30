from tkinter import *

def add_task():
    task = entry.get()
    if task.strip() != "":
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def clear_list():
    listbox.delete(0, END)


root = Tk()
root.title("To-Do List")

listbox = Listbox(root, height=10, width=50,)
listbox.place(x=5, y=20)


entry = Entry(root, width=50)
entry.place(x=5, y=200)

label=Label(root, text = "To Do List", bg="pink" , fg="black", height=1,width=30).place(x=40,y=0)

labe2=Label(root, text = "Enter your task here" ,bg="Pink" , fg= "Black",height=1, width =30).place(x=40,y=180)


add_button = Button(root, text="Add Task", command=add_task,bg="green")
add_button.place(x=5, y=240)

delete_button = Button(root, text="Delete Task", command=delete_task,bg="red")
delete_button.place(x=110, y=240)

clear_button = Button(root, text="Clear List", command=clear_list)
clear_button.place(x=240, y=240)


root.mainloop()