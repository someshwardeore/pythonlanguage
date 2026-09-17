class Student:
    college_name="RCP"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    @classmethod
    def change(cls,college_name):
        cls.college_name=college_name

    def display(self):
        print(self.college_name) 

s1=Student("someshwar",40) 
s1.change("RCCOEP")  
s1.display()           