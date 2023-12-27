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
        return f"""{self.get_name} {self.get_info} {self.get_price}"""
    
    @property
    def get_name_price(self):
        return f"""{self.get_name} {self.get_price}"""
    

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
        self.orders = dict()

    def show_products(self):
        for id, product in enumerate(self.products):
           print("*"*40)
           print("* {:<36} *".format(f"{id+1} - {product}"))
        print("*"*40)

    def addProduct(self, new_product):
        self.products.append(new_product)



