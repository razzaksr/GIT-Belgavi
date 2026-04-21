class Bank():
    number=0
    balance=1200
    statement = []
    def enq(self):pass
    def withdraw(self, amount):pass
    def deposit(self, amount):pass
    @staticmethod
    def choose(mode):
        if mode == "atm": return ATM()
        elif mode=="wallet": return Wallet()
        else: return Bank()
class ATM(Bank):
    _pin = 1222
    def enq(self):
        return self.balance
    def withdraw(self, amount):
        user = int(input("pin "))
        if user == self._pin:
            if amount<=self.balance: 
                self.balance -= amount
                print("debit",amount,"ok")
                self.statement.append("debit "+str(amount)+" via ATM")
            else: print("insufficient")
        else:print("wrong pin")
    def deposit(self,amount):
        self.balance+=amount
        print(amount,"deposited")
        self.statement.append("credit "+str(amount)+" via ATM")
class Wallet(Bank):
    __upi = 1111
    def enq(self): return self.balance
    def withdraw(self, amount):
        user = int(input("pin "))
        if user == self.__upi:
            if amount+10<=self.balance: 
                self.balance -= amount+10
                print("debit",amount,"ok")
                self.statement.append("transfer "+str(amount)+" via Wallet")
            else: print("insufficient")
        else:print("wrong pin")

print(Bank.choose("atm").enq())
Bank.choose("wallet").withdraw(900)
Bank.choose("atm").deposit(3400)
print(Bank.choose("bank").statement)
