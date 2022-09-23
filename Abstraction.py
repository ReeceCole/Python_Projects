from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
    @abstractmethod
    def payment(self, amount):
        pass
#this function needs an argument to be passed through it.
#When given a unknown data type.

class DebitCardPayment(car):
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $300 limit '.format(amount))
#this child class has defined how to implement the payment function from the parent class


obj = DebitCardPayment()
obj.paySlip("$800")
obj.payment("$800")
    
