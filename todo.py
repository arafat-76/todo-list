tasks=[]
while True:
    print("1.add task")
    print("2.show task")
    print("3.delete task")
    print("4.mark done")
    print("5.quit")
    choice=input("choose:")
    if choice=="1":
        task=input("enter your task: ")
        tasks.append(task)
        print("task added: ")

    elif choice=="2":
        for i,t in enumerate(tasks):
            print(i+1,t)

    elif choice=="3":
        task=input("which task to delete: ")
        if task in tasks:
            tasks.remove(task)
            print("task deleated: ")

    elif choice=="4":
        task=input("which task is done: ")
        if task in tasks:
            print("task is marked done: ")

    elif choice=="5":
        break

