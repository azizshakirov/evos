class Product:
    def __init__(self, name: str, info: str, price: float) -> None:
        self.name = name
        self.info = info
        self.price = price

    @property
    def get_name(self):
        return self.name
    
    @property
    def get_info(self):
        return self.info
    
    @property
    def get_price(self):
        return self.price
    
    def __str__(self):
        return f"""{self.get_name} 
{self.get_info} 
{self.get_price}
"""
    

class Market:
    def __init__(self, name, location, phone_number) -> None:
        self.name = name
        self.location = location
        self.phone_number = phone_number
        self.staff = None
        self.products = [
            Product('Lavash', "Hamir, Go'sht", 25000),
            Product('Hot Dok', "Hamir, Sosiska", 15000),
            Product('Burger', "Hamir, Go'sht", 35000)
        ]

    def show_products(self):
       [print(product) for product in self.products]

# p1 = 

# print(p1.get_name)

m1 = Market("EVOS", "Halqobod", "+998977777777")
m1.show_products()
