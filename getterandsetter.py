class Student:
    def __init__(self,marks):
        self.__marks=marks

    def setter(self,marks):
        if marks>=101:
            print("invalid marks")
        else:
            self.__marks=marks
            
    def getter(self):
        return self.__marks

s1=Student(100)
s1.setter(80)
print(s1.getter())   