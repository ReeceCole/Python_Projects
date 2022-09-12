#Parent Class User
class User:
    name = "Mark"
    email = "mark@gmail.com"
    pin_number = "3980"

    def getLoginInfo(self):
            entry_name = input("Enter your name: ")
            entry_email = input("Enter your email: ")
            entry_pin = input("Enter your pin: ")
            if (entry_email == self.email and entry_pin == self.pin_number):
                 print("Welcome back, {}!".format(entry_name))
            else:
                print("The password or email is incorrect.")
            
#Child Class Employee       
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

#Child Class Cook Employee
class Cook(User):
    base_pay = 9.00
    department = "Kitchen"
    pin_number = "3981"

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

cook = Cook()
cook.getLoginInfo()
