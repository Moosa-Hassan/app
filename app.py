class Task:

    def __init__ (self, details, due_date,count):
        self.details =details
        self.status = "Not Started"
        self.due_date = due_date
        self.count = count

    def update_status(self,status):
        self.status = status

    def update_due_date(self,due_date):
        self.due_date = due_date

    def print_task(self):
        print(self.count, " ", self.details," ", self.status, " ", self.due_date)
       
        




def display_menu():
    print("Press 1 to view all tasks")
    print("Press 2 to add a task")
    print("Press 3 to update the status of task")
    print("Press 4 to update the status of task")
    print("Press 5 to exit the app")



Task_in_list =0
print("To Do List")
tasks = []
while (True):
    print(" ")
    display_menu()
    choice = int(input())
    if (choice == 1):
        print("Details, Status, Due Date")
        count =0
        for task in tasks:
            task.print_task()
            count+= 1

    elif (choice == 2):
        detail = input("Enter details of the task : ")
        due = input("Enter the due date of the task: ")
        task = Task(detail,due,(Task_in_list))
        tasks.append(task)
        Task_in_list += 1

    elif (choice == 3):
        count =0
        for task in tasks:
            task.print_task()
            count+= 1
        num = int(input("Which Task would you like to update? Enter its number"))
        count =0
        status = input("Enter new Status : ")
        for task in tasks:
            if (tasks[count].count == num):
                tasks[count].update_status(status)
                break
            count+= 1

    elif (choice == 4):
        count =0
        for task in tasks:
            task.print_task()
            count+= 1
        num = int(input("Which Task would you like to update? Enter its number"))
        count =0
        due = input("Enter new Due Date : ")
        for task in tasks:
            if (task.count == num):
                task.update_due_date(due)
                break
            count+= 1
    elif (choice == 5):
        break