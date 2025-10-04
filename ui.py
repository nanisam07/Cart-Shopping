import tkinter as tk
from tkinter import messagebox
from cart import products, cart, add_to_cart, remove_from_cart, checkout, search_products

def run_ui():
    root = tk.Tk()
    root.title("🛍 Shosys")
    root.geometry("950x550")
    root.config(bg="#f5f5f5")

    # --- FUNCTIONS ---
    def update_cart_sidebar():
        cart_listbox.delete(0, tk.END)
        total = 0
        for item in cart:
            subtotal = item['price'] * item['quantity']
            total += subtotal
            cart_listbox.insert(tk.END, f"{item['name']} x {item['quantity']} = ₹{subtotal}")
        total_label.config(text=f"TOTAL: ₹{total}")

    def show_all_products():
        product_listbox.delete(0, tk.END)
        for p in products:
            product_listbox.insert(tk.END, f"{p['id']} - {p['name']} (₹{p['price']})")

    def search_item():
        keyword = entry_search.get()
        results = search_products(keyword)
        product_listbox.delete(0, tk.END)
        if not results:
            messagebox.showinfo("Search", "No products found")
            return
        for p in results:
            product_listbox.insert(tk.END, f"{p['id']} - {p['name']} (₹{p['price']})")

    def add_selected():
        try:
            selection = product_listbox.get(tk.ACTIVE)
            if not selection:
                messagebox.showwarning("Error", "No product selected")
                return
            pid = int(selection.split(" - ")[0])
            qty = int(entry_qty.get())
            add_to_cart(pid, qty)
            update_cart_sidebar()
            messagebox.showinfo("Success", "Item added to cart")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def remove_selected():
        try:
            selection = cart_listbox.get(tk.ACTIVE)
            if not selection:
                messagebox.showwarning("Error", "No item selected")
                return
            # extract product name
            pname = selection.split(" x ")[0]
            # find product id
            pid = next((item['id'] for item in cart if item['name'] == pname), None)
            if pid:
                remove_from_cart(pid)
                update_cart_sidebar()
                messagebox.showinfo("Removed", f"{pname} removed from cart")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def do_checkout():
        if not cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty!")
            return
        checkout()
        update_cart_sidebar()
        messagebox.showinfo("Checkout", "🎉 Purchase complete! Thank you.")

    # --- HEADER ---
    header = tk.Label(root, text="🛍 Welcome to Shopping Cart", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white", pady=10)
    header.pack(fill="x")

    # --- LEFT PANEL (CART) ---
    frame_left = tk.Frame(root, width=350, bg="white", bd=2, relief="groove")
    frame_left.pack(side="left", fill="y", padx=10, pady=10)

    tk.Label(frame_left, text="🛒 Your Cart", font=("Arial", 14, "bold"), bg="white", fg="#333").pack(pady=10)

    cart_listbox = tk.Listbox(frame_left, width=40, height=20, bg="#fafafa", fg="#222", font=("Arial", 11))
    cart_listbox.pack(padx=10, pady=5)

    total_label = tk.Label(frame_left, text="TOTAL: ₹0", font=("Arial", 12, "bold"), bg="white", fg="#d32f2f")
    total_label.pack(pady=5)

    tk.Button(frame_left, text="Remove Selected", command=remove_selected, bg="#e53935", fg="white", font=("Arial", 11, "bold"), width=20).pack(pady=5)
    tk.Button(frame_left, text="Buy / Checkout", command=do_checkout, bg="#43a047", fg="white", font=("Arial", 11, "bold"), width=20).pack(pady=5)

    # --- RIGHT PANEL (PRODUCTS) ---
    frame_right = tk.Frame(root, bg="white", bd=2, relief="groove")
    frame_right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    tk.Label(frame_right, text="🔍 Search Product:", font=("Arial", 12, "bold"), bg="white").pack(pady=5)
    entry_search = tk.Entry(frame_right, width=35, font=("Arial", 11))
    entry_search.pack(pady=5)
    tk.Button(frame_right, text="Search", command=search_item, bg="#0288d1", fg="white", font=("Arial", 11, "bold")).pack()

    tk.Label(frame_right, text="📦 Available Products:", font=("Arial", 13, "bold"), bg="white", fg="#333").pack(pady=10)
    product_listbox = tk.Listbox(frame_right, width=50, height=15, bg="#fafafa", fg="#111", font=("Arial", 11))
    product_listbox.pack(pady=5)

    tk.Label(frame_right, text="Quantity:", font=("Arial", 11), bg="white").pack(pady=5)
    entry_qty = tk.Entry(frame_right, width=10, font=("Arial", 11))
    entry_qty.pack(pady=5)

    tk.Button(frame_right, text="Add Selected to Cart", command=add_selected, bg="#1976d2", fg="white", font=("Arial", 11, "bold"), width=25).pack(pady=5)
    tk.Button(frame_right, text="Show All Products", command=show_all_products, bg="#616161", fg="white", font=("Arial", 11, "bold"), width=25).pack(pady=5)

    # Load initial products
    show_all_products()
    update_cart_sidebar()


    root.mainloop()
