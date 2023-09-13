import datetime

# Словарь для хранения задач
tasks = []

def add_task():
    description = input("Введите описание задачи: ")
    deadline_str = input("Введите срок выполнения (гггг-мм-дд чч:мм): ")
    try:
        deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Неверный формат срока выполнения. Используйте гггг-мм-дд чч:мм.")
        return

    task = {'description': description, 'deadline': deadline, 'done': False}
    tasks.append(task)
    print("Задача добавлена!")

def view_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for idx, task in enumerate(tasks, start=1):
            status = "Готово" if task['done'] else "В процессе"
            print(f"{idx}. Описание: {task['description']}, Срок: {task['deadline']}, Статус: {status}")

def mark_done():
    view_tasks()
    task_idx = int(input("Введите номер задачи, которую хотите отметить как выполненную (0 - вернуться): "))
    if task_idx == 0:
        return
    if 1 <= task_idx <= len(tasks):
        tasks[task_idx - 1]['done'] = True
        print("Задача отмечена как выполненная.")
    else:
        print("Неверный номер задачи.")

while True:
    print("\nМенеджер задач")
    print("1. Добавить задачу")
    print("2. Просмотреть задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Выйти")
    choice = input("Выберите действие: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

