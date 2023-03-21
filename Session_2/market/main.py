from market.cart import Cart
from market.item import Item

def main():
    # Create a new cart object
    cart = Cart()

    # Prompt the user to add and remove items
    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. Get total price")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            item = Item(name, price, quantity)
            cart.add_item(item)
            print(f"{item} added to cart.")
        elif choice == "2":
            name = input("Enter item name: ")
            for item in cart.items:
                if item.name == name:
                    cart.remove_item(item)
                    print(f"{item} removed from cart.")
                    break
            else:
                print(f"No item named {name} in cart.")
        elif choice == "3":
            print(f"The total price is {cart.get_total_price()}.")
        else:
            break
        