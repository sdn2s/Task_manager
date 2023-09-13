import tkinter as tk
from tkinter import messagebox
import datetime

# Создаем главное окно
root = tk.Tk()
root.title("Менеджер задач")

# Словарь для хранения задач
tasks = []

def add_task():
    description = entry_description.get()
    deadline_str = entry_deadline.get()

    try:
        deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d %H:%M')
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный формат срока выполнения. Используйте гггг-мм-дд чч:мм.")
        return

    task = {'description': description, 'deadline': deadline, 'done': False}
    tasks.append(task)

    listbox_tasks.insert(tk.END, f"{description} (Срок: {deadline_str})")

    entry_description.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)

def mark_done():
    selected_task_idx = listbox_tasks.curselection()
    if not selected_task_idx:
        return

    task_idx = selected_task_idx[0]
    tasks[task_idx]['done'] = True
    listbox_tasks.itemconfig(task_idx, {'bg':'light green'})

def view_tasks():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "Готово" if task['done'] else "В процессе"
        listbox_tasks.insert(tk.END, f"{task['description']} (Срок: {task['deadline']}, Статус: {status})")

# Создаем интерфейсные элементы
label_description = tk.Label(root, text="Описание:")
label_description.pack()

entry_description = tk.Entry(root, width=50)
entry_description.pack()

label_deadline = tk.Label(root, text="Срок выполнения (гггг-мм-дд чч:мм):")
label_deadline.pack()

entry_deadline = tk.Entry(root, width=50)
entry_deadline.pack()

button_add = tk.Button(root, text="Добавить задачу", command=add_task)
button_add.pack()

button_done = tk.Button(root, text="Отметить как выполненное", command=mark_done)
button_done.pack()

listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack()

button_view = tk.Button(root, text="Просмотреть задачи", command=view_tasks)
button_view.pack()

root.mainloop()
