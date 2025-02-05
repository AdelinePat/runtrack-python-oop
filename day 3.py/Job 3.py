class Task():
    def __init__(self, title, description, status="to do"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList():
    def __init__(self):
        self.list = []

    def add_task(self, new_task):
        self.list.append(new_task)
    
    def remove_task(self, task):
        self.list.remove(task)

    def set_task_status(self, task):
        if task in self.list:
            if task.status == "to do":
                task.status = "done"
            else:
                task.status = "to do"

    def display_tasks_list(self):
        display_string = ""
        for task in self.list:
            if task.status == "to do":
                display_string += "[ ] " + task.status.upper() + " : " + task.title + " → " + task.description + "\n"
            else:
                display_string += "[x] " + task.status.upper() + " : " + task.title + " → " + task.description + "\n"
        return display_string
    
    def filter_list(self, status):
        display_string = ""
        for task in self.list:
            if task.status == status:
                
                display_string += "• " + task.title + "\n"
        return f"{status.upper()} : \n{display_string}"


eat = Task("manger", "il faut manger à midi", "to do")
sleep = Task("dormir", "il faut dormir la nuit", "to do")
sport = Task("faire du sport", "il faut faire de l'exercice régulièrement", "to do")
exercice = Task("runtrack", "il faut finir sa runtrack du jour")
lessive = Task("lessive", "il faut faire la lessive au plus vite")
courses = Task("faire les courses", "il faut faire les courses pour pouvoir manger !")


to_do_list = ToDoList()
to_do_list.add_task(eat)
to_do_list.add_task(sleep)
to_do_list.add_task(sport)
to_do_list.add_task(exercice)
to_do_list.add_task(lessive)
to_do_list.add_task(courses)

to_do_list.set_task_status(eat)
to_do_list.set_task_status(lessive)
to_do_list.set_task_status(exercice)



print(to_do_list.display_tasks_list())
print(to_do_list.filter_list("to do"))

to_do_list.remove_task(sleep)
print(to_do_list.display_tasks_list())



