class Student:
    def __init__(self,name):
        self.name=name

    def get(self):
        return self.name

    def set(self,name):
        self.name=name
        print(self.name)   

s1=Student("someshwar") 

print(s1.get())

s1.set("yashodip")