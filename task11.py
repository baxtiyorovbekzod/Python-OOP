class Book:

    def __init__(self, title ,author, is_read ):
        self.name_book = title
        self.name_user = author
        self.is_read = is_read

    def mark_as_read(self):
           self.is_read = True
           print("Kitob o‘qilgan deb belgilandi" )

    def status(self):
       if self.is_read:
            print("Kitob o'qilgan") 
       else:
            print("Kitob o''qilmagan")

t1=Book("Bekorchilik", "O'zim😂", False)

t1.mark_as_read()
t1.status()
