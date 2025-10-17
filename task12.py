class BankAccount:

    def __init__(self, owner, balance ):
        self.owner = owner
        self.balance = balance

    def deposit( self, amount):
        self.balance += amount
        print(self.balance, "so'm")

    def  withdraw( self, amount):
          self.balance -= amount
          print(self.balance, "so'm" )

    def show_balance(self):
        print(self.balance, "so'm")   

t1=BankAccount("Bekzod", 500 )
t2=BankAccount("Azizbek", 400 )
t3=BankAccount("Muhammad Ali", 600 )


t1.deposit(200)
t1.withdraw(400)
t1.show_balance()
print()
t2.deposit(200)
t2.withdraw(300)
t2.show_balance()
print()
t3.deposit(200)
t3.withdraw(100)
t3.show_balance()