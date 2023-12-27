def admin_menu():
    while True:
        print("1. Ko'rish.")
        print("2. Qo'shish.")
        print("3. Chiqish.")
        n = int(input(">>> "))
        if n == 1:
            print("Ko'rishga kirdiz.")
        elif n == 2:
            print("Qoshishga kirdiz.")
        elif n == 3:
            break
    
def client_menu():
    while True:
        print("1. Ko'rish.")
        print("2. Buyurtma berish.")
        print("3. Chiqish.")
        n = int(input(">>> "))
        if n == 1:
            print("Ko'rishga kirdiz.")
        elif n == 2:
            print("Buyurtma tayyor.")
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


menu()