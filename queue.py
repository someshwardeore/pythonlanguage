queue=[]
max_size=5

while True:
    print("queue menu:")
    print("1. insert")
    print("2. delete")
    print("3. display")
    print("4. exit")

    choice=int(input("Enter Your Choice :"))
    if choice==1:
        if len(queue)>=5:
            print("queue is overflow")

        else:
            value=int(input("add element :"))
            queue.append(value)

    elif choice==2:
        if len(queue)==0:
            print("queue is underflow")

        else:
            value=int(input("delete element"))
            queue.pop(value)

    elif choice==3:
        print(queue)

    elif choice==4:
        print("program is end..")

    else:
        print("invalid choice")                                