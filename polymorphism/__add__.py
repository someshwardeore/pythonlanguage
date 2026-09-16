class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(f"{self.real} + {self.img}i") 

    def __add__(self,other):
        real=self.real+other.real
        img=self.img+other.img
        return Complex(real,img)    

num1=Complex(4,8)
num1.show()

num2=Complex(2,5)
num2.show()

num3=num1+num2
num3.show()