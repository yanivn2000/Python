
class BankAccount(object):
    commision = 5.6 #Class variable (inside and outside), like static

    def __init__(self, clientName, clientId, balance):
        self._clientName = clientName
        self._clientId = clientId
        self._balance = balance

    def withdraw(self, amount):
        if(self._balance - amount > 0):
            self._balance -= (amount + BankAccount.commision)
            return True
        return

    def deposit(self, amount):
        self._balance += (amount - BankAccount.commision)

    def __str__(self):
        return f"Client {self._clientId}, {self._clientName} has {self._balance} $"



ba = BankAccount("Yaniv Nuriel", "019283746", 1000)
ba.deposit(500)
print(ba.withdraw(100)) # True
#print(ba.withdraw(2000)) # None

print(ba) #1494.4 $
print(BankAccount.commision) #5.4
