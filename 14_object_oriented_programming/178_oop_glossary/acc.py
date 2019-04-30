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


class Checking(Account): # Checking sub class Account base class
    """ This class generates checking account objects """    

    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee


jack_checking=Checking("account\\jack.txt", 1)        
jack_checking.deposit(10)
jack_checking.transfer(110)
print(jack_checking.balance)
jack_checking.commit()
print(jack_checking.type)

johns_checking=Checking("account\\john.txt", 1)        
johns_checking.deposit(10)
johns_checking.transfer(110)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)


# class içinde yazılmış olan yorum satırlarını bize geriye döndürür
print(jack_checking.__doc__)