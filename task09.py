class User:

    def __init__(self, username, email, is_active ):
        self.username = username
        self.email = email
        self.is_active= is_active
    
    def activate(self):
         self.is_active == True
         print(f"Foydalanuvchi '{self.username}' faollashtirildi ")
            
    def deactivate(self):
        self.is_active = False
        print(f"Foydalanuvchi '{self.username}' bloklandi ")

t1=User("bekzod2404","bek2405@gmail.com", False)

t1.activate()    
t1.deactivate() 



   