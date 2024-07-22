import tkinter as tk
from tkinter import messagebox
import os

TASK_FILE = "tasks.txt"

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0,tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning","You Must Enter A Task")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning","You must select a task.")

def mark_complete():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.itemconfig(selected_task_index, {'bg' : 'lightgreen'})
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning","You must select a task.")


def save_tasks():
    tasks = task_listbox.get(0,tk.END)
    with open(TASK_FILE,"w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,"r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())


window = tk.Tk()
window.title("To-Do List")
window.geometry("300x400")
window.config(bg="lightblue")

task_listbox = tk.Listbox(window, width=25, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

task_entry = tk.Entry(window,width=20)
task_entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task, bg="green", fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task, bg="red", fg="white")
delete_button.pack(pady=5)

complete_button = tk.Button(window, text="Mark Completed", command=mark_complete, bg="blue", fg="white")
complete_button.pack(pady=5)

load_tasks()

window.mainloop()