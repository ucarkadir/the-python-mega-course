class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def witdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount 
     

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

# Checking sub class Account base class
class Checking(Account): 

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

checking=Checking("account\\balance.txt", 1)        
checking.deposit(10)
checking.transfer(110)

print(checking.balance)
# print(checking.transfer)

checking.commit()