# A To-Do List application 
print("Welcome to the To-Do List Application !")
print("1 - Create a Task")
print("2 - Mark Task as done")
print("3 - Show the To-Do List")
print("4 - Exit")
bool=True
t_list=[]
while bool:
    choice=int(input("Enter the choice you want to perform : "))
    bool=True
    if choice==1:
        task=input("Enter the task to be created :")
        t_list.append(task)
    elif choice==2:
        if len(t_list)==0:
            print("The To-Do list Empty!")
        else:    
            print("The tasks in To-Do List are :")
            c=1
            for i in t_list:
                print(c,".",i)
                c+=1        
        task=int(input("Enter the task number you finished :"))
        val=task-1
        if  val<len(t_list):
            t_list.pop(val)
        else:
            print("Sorry the task mentioned is not available in the To-Do List")
    elif choice==3:
        if len(t_list)==0:
            print("The To-Do list Empty!")
        else:    
            print("The tasks in To-Do List are :")
            c=1
            for i in t_list:
                print(c,".",i)  
                c+=1      
    else:
        print("Thank you for using our To-Do List Application")
        bool=False
