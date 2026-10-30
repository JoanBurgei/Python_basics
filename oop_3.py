# bank account==owner,acc no ,balance, statement/history
from datetime import date, datetime  # ctrl and open it
# from sys import dont_write_bytecode
# from time import strPtime


class Client:
    def __init__(self, names:str, kra_pin, dob, gender:str):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.names)
        print(self.kra_pin)
    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob,'%Y-%m-%d')
        age = today.year - birth_date.year
        return age

class BankAccount:
    def __init__(self, owner, balance:int, acc_no:str):
        self.owner = owner
        self.balance = balance
        self.acc_no = acc_no

    def deposit(self, amount):
        self.balance += abs(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner.names)
        # self.owner.print_details()
        print(self.acc_no)
        print(self.balance)
        print("------------------")

#ctrl+alt+l formats your code
#All the code above is material, now let us build an actual bank
#owner 1

Joan = Client("Joan Njeri", "A002", "1996-12-11", "f")
Ahmed = Client("Ahmed Kabul", "A001", "2000-03-24", "m")

acc1 = BankAccount(Joan,acc_no="123409", balance=70_000)
acc2 = BankAccount(Ahmed,acc_no="567890", balance=30_000)
acc3 = BankAccount(Joan,acc_no="11111", balance=40_000)

acc1.deposit(10_000)
acc2.deposit(30_000)
acc1.print_details()

acc1.withdraw(5_000)
# acc2.withdraw(30_000)
acc1.print_details()

print("Joan_Age", Joan.calc_age())
print("Ahmed_Age", Ahmed.calc_age())

print(acc1.owner.names, acc1.owner.calc_age())
print(Joan.names,Joan.calc_age())

#DATE
# dob = '18-07-1962'#d.m.y hh.mm.ss
# today = date.today()
# # print(today)#today.year/month/day
# # print(f"{today.year}-{today.month}-{today.day}")
# #convert string to date
# birth_date = datetime.strptime(dob,'%d-%m-%Y')
#
# age = today.year - birth_date.year
# print(age)
