
class BankAccount(object):
    commision = 5.6 #Class variable (inside and outside), like static

    def __init__(self, clientName, clientId, balance):
        self._clientName = clientName
        self._clientId = clientId
        self._balance = balance

    def withdraw(self, amount):
        if(self._balance - amount > 0):
            self._balance -= (amount - BankAccount.commision)
            return True
        return

    def deposit(self, amount):
        self._balance += (amount - BankAccount.commision)

    def __str__(self):
        return f"Client {self._clientId}, {self._clientName} has {self._balance} $"


class StudentBankAccount(BankAccount):
    def __init__(self, clientName, clientId, balance, collageName):
        #slide #16: better use supper() because it is implicit call to the parent rather explicit call to the class name
        BankAccount.__init__(self, clientName, clientId, balance)
        self._collageName = collageName

    def __str__(self):
        return f"Student {self._clientId}, {self._clientName} from Collage {self._collageName} has {self._balance} $"

ba = StudentBankAccount("Yaniv Nuriel", "019283746", 1000, "Sela")
ba.deposit(500)
print(ba) #1500
