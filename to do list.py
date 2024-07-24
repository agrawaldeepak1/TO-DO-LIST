import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, win):
        self.win = win
        self.win.title("To-Do List")
        self.win.geometry("400x500")
        self.win.resizable(False,False)
        self.win.configure(background="black")  

        self.list_frame = tk.Frame(self.win, bg="yellow")  
        self.list_frame.pack(fill="both", expand=True)

        self.task_list = tk.Listbox(self.list_frame, width=40, bg="black", fg="white")  
        self.task_list.pack(fill="both", expand=True)

        self.input_frame = tk.Frame(self.win, bg="red")  
        self.input_frame.pack(fill="x")

        self.task_entry = tk.Entry(self.input_frame, width=35, bg="yellow", fg="red")
        self.task_entry.pack(side="left")

        self.add_button = tk.Button(self.input_frame, text="Add", command=self.add_task, bg="brown", fg="white")  
        self.add_button.pack(side="left")

        self.delete_button = tk.Button(self.input_frame, text="Delete", command=self.delete_task, bg="darkgreen", fg="white")  
        self.delete_button.pack(side="left")

        self.save_button = tk.Button(self.input_frame, text="Save", command=self.save_tasks, bg="blue", fg="white")  
        self.save_button.pack(side="left")

        self.clear_button = tk.Button(self.input_frame, text="Clear", command=self.clear_tasks, bg="red", fg="white")  
        self.clear_button.pack(side="left")

        self.exit_button = tk.Button(self.input_frame, text="Exit", command=self.win.quit, bg="#e74c3c", fg="white")  
        self.exit_button.pack(side="left")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert("end", task)
            self.task_entry.delete(0, "end")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
        except:
            messagebox.showinfo("Error", "Select a task to delete")

    def save_tasks(self):
        tasks = self.task_list.get(0, "end")
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully")

    def clear_tasks(self):
        self.task_list.delete(0, "end")

win = tk.Tk()
app = ToDoList(win)
win.mainloop()