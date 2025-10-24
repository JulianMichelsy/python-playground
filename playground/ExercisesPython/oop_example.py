class Task:
    def __init__(self, id, title):
        self.id = id 
        self.title = title
        self.done = False 
            # Task is not done by default 

    def toggle(self):
        """
        Toggle the task status 
        """
        self.done = not self.done 
            # False --> True OR True --> False
    def __repr__(self):
        """
        text representation for task print
        """
        status = "Check" if self.done else "Uncheck"
        return f"{status} ({self.id} {self.title})"
    
class TaskManager:
    def __init__(self):
        self.tasks = []
            # All the tasks are here 

    def add(self, task):
        """
        Add a task to the list
        """
        self.tasks.append(task)

    def remove(self, task_id):
        """
        Remove a task by id 
        """
        self.task = [t for t in self.tasks if t.id != task_id]

    def list_pending(self):
        """
        shows uncompleted tasks
        """
        return [t for t in self.tasks if not t.done]
    
# --- Test ---
if __name__ == "__main__":
    t1 = Task(1, "Learn python")
    t2 = Task(2, "Practice git")

    manager = TaskManager()
    manager.add(t1)
    manager.add(t2)

    t1.toggle()
        # Toggle t1 to True(Done) because it's False(Not done) by default

    assert(len(manager.tasks) == 2)
    assert(len(manager.list_pending()) == 1)
    print("oop_example Works properly.")