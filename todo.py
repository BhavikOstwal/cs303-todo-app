# todo.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

# BUG FIX: Added header and ensured clean numbering
def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("--- Your Tasks ---")
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')
        print(f"Total: {len(tasks)} task(s)")


if __name__ == "__main__":
    add_task("Finish Assignment")
    list_tasks()
