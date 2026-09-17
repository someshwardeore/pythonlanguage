class Calculator:

    @staticmethod
    def add(num1,num2):
        return num1+num2

    @staticmethod
    def even(n):
        if n%2==0:
            return True

        else:
            return False

# print(Calculator.add(10,20))
# print(Calculator.even(7))        
c1=Calculator()
print(c1.add(10,20))
print(c1.even(5))