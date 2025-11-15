
cart = []
while True:
    response = input("Do you want to add item to the cart? ")
    if response.lower() != "yes":
        break
    item = input("Enter item: ")
    cart.append(item)
print("Your cart contains:", cart)