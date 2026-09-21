class Student:
    name="someshwar"
    @classmethod
    def display(cls,name):
        cls.name=name
        super().name="yashodip"

S1=Student()
S1.display("Yashodip")

print(S1.name)