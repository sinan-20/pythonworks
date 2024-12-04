# Bank [acno,balance,ac_type,costmr_name] [initialize,deposit(amount)mwithdaw(amount),get_balance()]

class Bank:

    ac_no:int

    balance:int

    ac_type:str

    costomer_name:str

    def __init__ (self,ac_no,balance,ac_type,costomer_name):

        self.ac_no=ac_no

        self.balance=balance

        self.ac_type=ac_type

        self.costomer_name=costomer_name

    def deposit(self,amount):

        self.balance+=amount

        print(f" Your account number{self.ac_no} has been credited  with amount {amount} avl balance{self.balance}")

    def withdraw(self,amount):

        if self.balance<amount:

            print("insufficient bank balance")

        else:

            self.balance-=amount

            print(f" Your account number{self.ac_no} has been debitted  with amount {amount} avl balance{self.balance}")


    def get_balance(self):

        print("your aval balance",self.balance)


bank_instance1=Bank(12212121,2500,"savings","sinan")

bank_instance1.withdraw(500)
bank_instance1.deposit(700)
bank_instance1.get_balance()




        