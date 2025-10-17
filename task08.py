class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ✅ ")
        else:
            print(f"{self.name} hozirda tugagan ❌ ")



product1 = Product("AirPods", 199, "Elektronika", True)
product2 = Product("iPhone 13", 898, "Elektronika", False)

product1.check_stock()  
product2.check_stock()  