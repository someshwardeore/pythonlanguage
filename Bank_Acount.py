class Bank_Acount:
    def __init__(self,balance,holder_name):
        self.__balance=balance
        self.holder_name=holder_name

    def debit(self,amount):
        print(f"amount is debited : {amount}")
        self.__balance+=amount
        print(f"total balance is : {self.__balance}")

    def credit(self,amount):
        print(f"amount is credited : {amount}") 
        self.__balance-=amount
        print(f"total balance is : {self.__balance}")
           

    def Balance(self):
        print(f"total amount is : {self.__balance}")

a=int(input("debit :"))
b=int(input("credit :"))
h1=Bank_Acount(5000,"someshwar")
h1.debit(a)
h1.credit(b)
h1.Balance()
          