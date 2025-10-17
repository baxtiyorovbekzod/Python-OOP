class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"Mahsulot: {self.name}, Narxi: {self.price} so'm ")



p1 = Product("AirPods", 1500000, "Elektronika")
p2 = Product("iPhone 15", 15000000, "Elektronika")
p3 = Product("Nike Air Max", 2200000, "Kiyim-kechak")
p4 = Product("MacBook Pro", 23000000, "Elektronika")
p5 = Product("Kofe mashinasi", 1800000, "Maishiy texnika")
p6 = Product("Samsung TV", 12000000, "Elektronika")


products = [p1, p2, p3, p4, p5, p6]


most_expensive = max(products, key=lambda product: product.price)



most_expensive.info()