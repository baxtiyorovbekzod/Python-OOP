class BankAccount:

    def __init__(self, owner, balance ):
        self.owner = owner
        self.balance = balance

    def deposit( self, amount):
        
        print(self.balance + amount , "so'm")

    def  withdraw( self, amount):
          
          print(self.balance - amount, "so'm" )
      

t1=BankAccount("Bekzod", 500 )

t1.deposit(200)
t1.withdraw(300)
