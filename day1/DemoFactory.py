class Card:
    def __init__(self):
        self.__cvv=122
        self.__limit = 20000
    def transaction(self,amount):
        user = int(input("enter the cvv"))
        if user == self.__cvv:
            if self.__limit>=amount: print("Transaction",amount,"successfull via Card")
            else: print("Insufficient Limit")
        else: print("Invalid CVV")
class UPI:
    def __init__(self):
        self.__pin = 9872
        self.__balance = 12000
    def transaction(self,amount):
        user = int(input("enter upi pin "))
        if user == self.__pin:
            if self.__balance>=amount: print("Transaction",amount,"made via UPI")
            else: print("Insufficient balance")
        else: print("Invalid UPI PIn")

class Amazon:
    @staticmethod
    def purchase(mode):
        if mode == "card": return Card()
        else: return UPI()
# main execution
# Amazon.purchase("upi").transaction(14000)
Amazon.purchase("card").transaction(14000)
        
