from cart import *

def menu():
    while True:
        print("""
===== Shopping Cart =====
1. View Products
2. Add to Cart
3. View Cart
4. Update Cart
5. Remove from Cart
6. Checkout
7. Exit
""")
        choice = input("Enter choice: ")
        if choice == "1":
            view_products()
        elif choice == "2":
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity: "))
            add_to_cart(pid, qty)
        elif choice == "3":
            view_cart()
        elif choice == "4":
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter New Quantity: "))
            update_cart(pid, qty)
        elif choice == "5":
            pid = int(input("Enter Product ID: "))
            remove_from_cart(pid)
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")
            
