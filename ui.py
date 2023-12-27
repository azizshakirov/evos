from main import *
from core import *


def admin_menu():
    while True:
        print("1. Ko'rish.")
        print("2. Qo'shish.")
        print("3. Chiqish.")
        n = int(input(">>> "))
        if n == 1:
            m1.show_products()
        elif n == 2:
            name = input("Nomi: ")
            info = input("Malumot: ")
            price = float(input("Narxi: "))
            product = Product(name, info, price)
            m1.addProduct(product)
        elif n == 3:
            break
    
def client_menu():
    while True:
        print("1. Ko'rish.")
        print("2. Buyurtma berish.")
        print("3. Chiqish.")
        n = int(input(">>> "))
        if n == 1:
            m1.show_products()
            c = int(input(">>> "))
            prod = m1.products[c-1]
            if prod in m1.orders:
                m1.orders[prod] += 1
            else :
                m1.orders[prod] = 1
        elif n == 2:
            Core.saveOrder(m1.orders)
        elif n == 3:
            break
def menu():
    print("1. Admin.")
    print("2. Mijoz.")
    print("3. Chiqish.")
    n = int(input(">>> "))
    if n == 1:
        admin_menu()
    elif n == 2:
        client_menu()


m1 = Market("EVOS", "Halqobod", "+998977777777")
menu()