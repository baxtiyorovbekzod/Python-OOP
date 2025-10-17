class Product:

    def __init__(self, name, price, category, in_stock ):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

t1=Product("Iphone 15", 400.5, "elektronics", True)
t2=Product("Xiaomi 15", 300.6, "elektronics", False)

print(f"nomi:{t1.name}")
print(f"narxi:{t1.price}")
print(f"categoriyasi:{t1.category}")
print(f"mahsulot mavjudligi:{t1.in_stock}") 

print()
print(f"nomi:{t2.name}")
print(f"narxi:{t2.price}")
print(f"categoriyasi:{t2.category}")
print(f"mahsulot mavjudligi:{t2.in_stock}") 
  