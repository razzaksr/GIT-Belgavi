'''
Encapsulation:
	Creditcard >> cardNumber, expiry, pin, cvv, cardholder
'''
class Patient:
    # _instance = None
    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = super(Patient, cls).__new__(cls)
    #     return cls._instance
    def __init__(self,name="",addr="", age=0, cont=0):
        self.__name = name
        self.__address = addr
        self.__age = age
        self.__contact = cont
    def get_name(self): return self.__name
    def get_address(self): return self.__address
    def get_age(self): return self.__age
    def get_contact(self): return self.__contact
    def set_name(self, name): self.__name = name
    def set_address(self, addr): self.__address = addr
    def set_age(self, age): self.__age = age
    def set_contact(self, cont): self.__contact = cont
    def __str__(self): return "Name: " + self.__name + "\nAddress: " + self.__address + "\nAge: " + str(self.__age) + "\nContact: " + str(self.__contact)
    
patient1 = Patient("Ton", age = 30)
patient2 = Patient("Jane", addr="123 Street")
patient3 = Patient("Jake", addr="123 Street", cont=1234567890)
patient1.__age=34 # not updated
patient1.set_age(34) # updated
print(patient1)
print(patient2.get_address())