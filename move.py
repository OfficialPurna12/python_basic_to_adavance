# Collect Book Store Information
print("📚 Welcome to the Book Store Info Collector 📚\n")

store_name = input("Enter your Book Store Name: ")
book_name = input("Enter your Book Name: ")
contact_number = input("Enter your Contact Number: ")
address = input("Enter your Address: ")

# Ensure book price is a valid number
# while True:
#     try:
#         book_price = float(input("Enter your Book Price (e.g., 299.99): "))
#         break
#     except ValueError:
#         print("❌ Invalid input. Please enter a number for the price.")

book_authority = input("Enter the Book Author's Name: ")
rating = input("Enter the Book Rating (e.g., 4.5/5): ")

# Display the collected information nicely
print("\n" + "="*40)
print(f"🏪 Store Name       : {store_name}")
print(f"📖 Book Name        : {book_name}")
print(f"📞 Contact Number   : {contact_number}")
print(f"🏠 Address          : {address}")
# print(f"💲 Book Price       : ${book_price:.2f}")
print(f"✍️  Author Name      : {book_authority}")
print(f"⭐ Book Rating       : {rating}")
print("="*40)
print("Thank you for visiting our library! 📚")
