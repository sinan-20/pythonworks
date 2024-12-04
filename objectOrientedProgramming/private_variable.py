class BankAccount:

    custemer_name:str

    mpin:int

    account_type:str

    balance:int

    def __init__(self,custemer_name,mpin,account_type,balance):

        self.custemer_name=custemer_name

        self.__mpin=mpin

        self.account_type=account_type

        self.__balance=balance

    def __str__(self):

        return self.custemer_name
    
    def get_balance(self):

        print(self.__balance)

bank_account_instance=BankAccount("SINAN",2314,"savings",56000)

print(bank_account_instance)

bank_account_instance.get_balance()