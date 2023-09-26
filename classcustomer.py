class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}({self.balance}원)"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

bill = Customer("Bill")
steve = Customer("Steve", 50000)
tim = Customer("Tim", 100000)

print(bill, steve, tim)

bill.deposit(50000)
steve.withdraw(20000)
tim.withdraw(100000)
print(bill, steve, tim)  

total_balance = bill.balance + steve.balance + tim.balance
print(total_balance)

steve.deposit(60000)
tim.withdraw(90000)
print(bill, steve, tim)  
