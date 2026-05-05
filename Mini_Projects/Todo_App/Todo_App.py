class Task:
    def __init__(self, description):
        self.description = description
        self.done = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def complete_task(self, index):
        self.tasks[index].done = True

    def remove_task(self, index):
        self.tasks.pop(index)

    def show_tasks(self):
        print('\n===== All tasks =====\n')
        for task in self.tasks:
            print(f'Description: {task.description}\n Status: {task.done}\n')

task_manager = TaskManager()

task_manager.add_task('Defeat the OOP')
task_manager.add_task('Learn classes and objects')
task_manager.add_task('Learn the principles of OOP')

task_manager.complete_task(0)
task_manager.complete_task(1)
task_manager.complete_task(2)

task_manager.show_tasks()
