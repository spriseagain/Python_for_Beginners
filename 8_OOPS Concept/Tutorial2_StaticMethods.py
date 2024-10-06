#Static Methods

#Methods that don't use the self parameter(work at class level)

class Student:

    #Static method (decorator)
    @staticmethod
    def hello(): 
        print("hello")


#Decorators allow us to wrap another function in order to extend the 
#the behaviour of the wrapped function, without permanently modifying it.


#Pillars of OOP Programming

#1.Abstraction
"""
Hiding the implementation details of a class
and only showing the essential features to the user
"""

class Car:

    def __init__(self) -> None:
        self.accelerator = False
        self.brk =False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car Started ..")

car1 = Car()
#car1.start() #abstraction

#2.Encapsulation


"""
Capsule of data and related function into a single unit(object)

Wrapping data and functions into a single unit(object)

"""

#WAP : Create Accont class with 2 attributes - balance & account no.
# Create methods for debit, credit and printing the balance

class Account:

    def __init__(self,account_num,balance) -> None:
        self.account_num = account_num
        self.balance = balance

    #debit method    
    def debit(self,amount):
        self.balance -=amount
        print(f"Rs {amount} was debited from account number {self.account_num}. Final balance = {self.get_bal()}")

    
    #credit method
    def credit(self,amount):
        self.balance +=amount
        print(f"Rs {amount} was credited to account number {self.account_num}. Final balance = {self.get_bal()}")


    def get_bal(self):
        return self.balance


acc1 = Account(1234,10000)
print(acc1.account_num,acc1.balance)

acc1.credit(150)

              

#3.Inhertence

#4.Polymorphism



