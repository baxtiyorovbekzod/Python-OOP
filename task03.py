class User:

    def __init__(self, username, email,is_active ):
        self.username = username
        self.email = email
        self.is_active= is_active


t1=User("bekzod2404","bek2405@gmail.com", True )


print(t1.username)
print(t1.is_active)
print(t1.email)
   