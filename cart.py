from products import products
cart = []

def search_products(keyword):
    results = [p for p in products if keyword.lower() in p['name'].lower()]
    return results

def view_products():
    print("\n===== Available Products =====")
    for p in products:
        print(f"{p['id']}. {p['name']} - ₹{p['price']}")
    print("==============================")

def add_to_cart(product_id, quantity):
    if len(cart) >= 8:
        print("❌ Cart limit reached (8 items max).")
        return
    for item in cart:
        if item['id'] == product_id:
            item['quantity'] += quantity
            print(f"✅ Updated {item['name']} quantity to {item['quantity']}")
            return
    for p in products:
        if p['id'] == product_id:
            cart.append({"id": p['id'], "name": p['name'], "price": p['price'], "quantity": quantity})
            print(f"✅ Added {p['name']} (x{quantity}) to cart")
            return
    print("❌ Invalid Product ID")

def view_cart():
    if not cart:
        print("\n🛒 Cart is empty!")
        return
    print("\n===== Your Cart =====")
    total = 0
    for item in cart:
        subtotal = item['price'] * item['quantity']
        total += subtotal
        print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
    print(f"=====================\nTOTAL: ₹{total}")

def update_cart(product_id, quantity):
    for item in cart:
        if item['id'] == product_id:
            item['quantity'] = quantity
            print(f"🔄 Updated {item['name']} to {quantity}")
            return
    print("❌ Item not found in cart")

def remove_from_cart(product_id):
    for item in cart:
        if item['id'] == product_id:
            cart.remove(item)
            print(f"🗑 Removed {item['name']}")
            return
    print("❌ Item not found")

def checkout():
    view_cart()
    cart.clear()
    print("🎉 Checkout complete! Thank you for shopping.")
