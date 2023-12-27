from datetime import datetime

from main import Product

class Core:

    @staticmethod
    def saveOrder(orders: dict):
        with open("orders.txt", 'a') as file:
            cur_date = datetime.now()
            s = ''
            for product, count in orders.items():
                s += f"{product.get_name_price} {count}|"
            s+= f"{cur_date}"
            file.write(s)