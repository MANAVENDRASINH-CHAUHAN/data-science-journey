class Account:


    def __init__(self,balance,account_num):
        self.balance = balance 
        self.account_num = account_num

    def debit(self,debit_amount):
        self.balance -= debit_amount
        return self.balance
        print("your total balance is :", self.getbalance())
        
    def credit(self,creadit_amount):
        self.balance += creadit_amount 
        return self.balance
        print("your total balance is :", self.getbalance())

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(5000)
