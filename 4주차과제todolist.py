import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)


root = tk.Tk()
root.title("To-Do 리스트")

label1 = tk.Label(root,text="Add a task:")
label1.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()


task_listbox = tk.Listbox(root, width=40)
task_listbox.pack()


delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()


root.mainloop()
