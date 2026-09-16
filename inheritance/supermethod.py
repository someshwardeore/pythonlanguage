class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"name is : {self.name}\nage is : {self.age}")    

class Student(Person):
    def __init__(self,name,age): 
        super().__init__(name,age) 
        super().info()

s1=Student("someshwar",18)