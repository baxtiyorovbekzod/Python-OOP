class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False   

    def mark_as_read(self):
        self.is_read = True
        print(f"{self.title}: bu kitob  o‘qilgan ✅")

    def status(self):
        if self.is_read:
            print(f"{self.title} – O‘qilgan  ✅")
        else:
            print(f"{self.title} – O‘qilmagan ❌")

book1 = Book("Bekorchilik san’ati", "O‘zim 😂")
book2 = Book("Python asoslari", "Python Asoschisi amaki")
book3 = Book("Yulduzlar orasida", "Bekzod Baxtiyorov")
book4 = Book("Aql va hissiyot", "Ustozim🤣")


book1.mark_as_read()
book4.mark_as_read()
print()

print("Kitoblar statusi")
book1.status()
book2.status()
book3.status()
book4.status()