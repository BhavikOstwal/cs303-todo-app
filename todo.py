# todo.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def list_tasks():
    if not tasks:
        print("No tasks available.")
    
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')


# NEW FEATURE: delete a task by index
def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f'Task "{removed}" deleted.')
    else:
        print("Invalid task number.")


if __name__ == "__main__":
    add_task("Finish Assignment")
    list_tasks()
