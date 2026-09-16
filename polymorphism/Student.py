class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __eq__(self,other):
        if(self.marks==other.marks):
            return True

        else:
            return False

s1=Student("someshwar",88)
s2=Student("krishna",90)

checkmarks=(s1==s2)
print(checkmarks)