class Rectangle:
    def  __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print(f"are is :{self.length*self.width}") 

length=int(input("Enter length of length:"))
width=int(input("Enter length of width:"))

R1=Rectangle(length,width) 
R1.area()          