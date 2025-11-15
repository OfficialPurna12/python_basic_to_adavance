
class Product:
    def __init__(self, name="", price=0.0):
        self.name = name
        self.price = price
    
    def input_data(self):
        self.name = input("Enter product name: ")
        try:
            self.price = float(input("Enter product price: "))
        except ValueError:
            print("Invalid price entered. Setting price to 0.0")
            self.price = 0.0
    
    def display_data(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: ${self.price:.2f}")

# Create an object of the Product class
product = Product()

# Accept input from the user
product.input_data()

# Display the entered product details
print("\nProduct Details:")
product.display_data()