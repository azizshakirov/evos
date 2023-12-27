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
    


p1 = Product('Lavash', "Hamir, Go'sht", 25000)

print(p1.get_name)