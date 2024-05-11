tasks=[]

def add_tasks(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
       tasks.remove(task)
    else:
       print("The entered task is not available")

def view_task():
   if tasks:
    for idx,task in enumerate(tasks,start=1):
      print(f"{idx}.{task}")
   else:
      print("No task is written")

def main():
 
 while True:
   print("\n 1.Add a task")
   print("2.Remove a task")
   print("3.View the task list")
   print("4.Exit")

   choice =input("Enter a choice from 1-4:")

   if choice == '1':
    task=input("Enter the task to be added:")
    add_tasks(task)

   elif choice == '2':
      
    task=input("Enter the task to be removed:")
    remove_task(task)

   elif choice == '3':
    view_task()

   elif choice =='4':
    print("Exiting program")
    break
   else:
    print("Invalid choice.Please enter the right choice")

if __name__ == "__main__":
    main()



    



    