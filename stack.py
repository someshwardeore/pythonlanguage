max_size=5
stack=[]

while True:
    print("stack menu is :")
    print("1. insert")
    print("2. delete")
    print("3. display")
    print("4. exit")

    choice=int(input("Enter your choice (1-4) : "))

    if choice==1:
        if len(stack)>max_size:
            print("stack is overflow")

        else:
            value=int(input("insert element in stack :"))
            stack.append(value)
            print(stack)

    elif choice == 2:
        if len(stack)==0:
            print("stack is under flow")

        else:
            value=int(input("Delete Element from stack : "))
            stack.pop(value)
            print(stack)

    elif choice == 3:
        print(stack.reverse())

    elif choice ==4:
        print("you are exit in program") 

    else:
        print("invalid choice")                               