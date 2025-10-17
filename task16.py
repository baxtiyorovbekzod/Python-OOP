class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False  

    def mark_as_read(self):
        self.is_read = True
        print(f" {self.title}: kitobi o‘qilgan deb belgilandi ✅")

    def status(self):
        if self.is_read:
            print(f"{self.title} – O‘qilgan ✅")
        else:
            print(f"{self.title} – O‘qilmagan ❌")



b1 = Book("Bekorchilik san’ati", "O‘zim 😂")
b2 = Book("Python asoslari", "Python asoschisi")
b3 = Book("Boy ota, kambag‘al ota", "Robert Lewandowski")
b4 = Book("Odam bo‘lish qiyin", "Ustozim 😂")
b5 = Book("Yulduzlar orasida", "O‘zim 😂")


books = [b1, b2, b3, b4, b5]


b1.mark_as_read()
b4.mark_as_read()

print()

print(" Barcha kitoblarning holati:")
for book in books:
    book.status()

print()

print(" O‘qilgan kitoblar:")
for book in books:
    if book.is_read:
        print( book.title)