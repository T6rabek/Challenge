import os
tasks = []

def add_task():
    user_task = input("Enter the name of the task: ")
    tasks.append(user_task)


def view_tasks():
    print('👇Here are your tasks: ')
    for index, task in enumerate(tasks, start=1):
        print(f"{index}.{task}")



def mark_done():
    print("Mark the tasks you want!\n\n")
    view_tasks()
    marking = int(input("Enter the number of task you want to mark: "))
    if 1<= marking <= len(tasks):
        tasks[marking - 1] += " ✔️"
        print(f"Task {marking} marked as done!")

    else:
        print("Please, enter a valid option")





def delete_tasks():
    view_tasks()

    deleting = int(input("Choose one of the options to delete: "))

    if 1<=deleting<=len(tasks):
        del tasks[deleting-1]
        print("Done :)")


    else:
        print("Please enter a valid option to delete!")



def saver():
    with open('task.txt', 'w') as file:
        for task in tasks:
            file.write(task + "\n")


def loading():
    if os.path.exists('task.txt'):
        with open('task.txt', 'r') as file:
            loaded_tasks = file.readlines()
            global tasks
            tasks = [task.strip() for task in loaded_tasks]
            print("Tasks loaded successfully!")
    else:
        print("No files found!")
        




def main():
    loading()
    while True:

        print("Hello and welcome to to-do-list program😊"
              "\n\nChoose one of the options below🔔")
        choice = int(input("\n1.Adding task"
                           "\n2.Viewing task"
                           "\n3.Marking task"
                           "\n4.Deleting task"
                           "\n5.Saving the list"
                           "\n6.Exit"
                           "\nChoice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_done()
        elif choice == 4:
            delete_tasks()
        elif choice == 5:
            saver()
        elif choice == 6:
            print("Thank you for choosing us!")
            break
        else:
            print("Please, enter a valid option!")




if __name__ == "__main__":
    main()