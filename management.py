# 📚 Mini Library Management System 📚

books = []  # list to store all books


def add_book():
    """Add a new book to the library"""
    store_name = input("Enter Store Name: ")
    book_name = input("Enter Book Name: ")
    contact_number = input("Enter Contact Number: ")
    address = input("Enter Address: ")

    # Validate price input
    while True:
        try:
            book_price = float(input("Enter Book Price (e.g., 299.99): "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    author = input("Enter Author Name: ")
    rating = input("Enter Book Rating (e.g., 4.5/5): ")

    book = {
        "Store Name": store_name,
        "Book Name": book_name,
        "Contact": contact_number,
        "Address": address,
        "Price": book_price,
        "Author": author,
        "Rating": rating
    }
    books.append(book)
    print("✅ Book added successfully!\n")


def view_books():
    """Display all books in table format"""
    if not books:
        print("⚠️ No books found!\n")
        return

    print("\n" + "=" * 80)
    print("📚 All Book Records 📚")
    print("=" * 80)
    print(f"{'ID':<3} {'Store Name':<15} {'Book Name':<20} {'Author':<15} {'Price':<10} {'Rating':<8}")
    print("-" * 80)

    for idx, b in enumerate(books, start=1):
        print(f"{idx:<3} {b['Store Name']:<15} {b['Book Name']:<20} {b['Author']:<15} "
              f"${b['Price']:<9.2f} {b['Rating']:<8}")

    print("=" * 80 + "\n")


def search_book():
    """Search book by name or author"""
    keyword = input("Enter Book Name or Author to search: ").lower()
    results = [b for b in books if keyword in b['Book Name'].lower() or keyword in b['Author'].lower()]

    if results:
        print("\n🔍 Search Results:")
        for b in results:
            print(f"- {b['Book Name']} by {b['Author']} (${b['Price']:.2f}, Rating: {b['Rating']})")
    else:
        print("❌ No matching book found.\n")


def update_book():
    """Update book details"""
    view_books()
    try:
        book_id = int(input("Enter Book ID to update: ")) - 1
        if 0 <= book_id < len(books):
            print("Leave blank if you don't want to change a field.")
            new_name = input(f"New Book Name ({books[book_id]['Book Name']}): ") or books[book_id]['Book Name']
            new_author = input(f"New Author ({books[book_id]['Author']}): ") or books[book_id]['Author']
            new_price = input(f"New Price ({books[book_id]['Price']}): ")
            new_price = float(new_price) if new_price else books[book_id]['Price']
            new_rating = input(f"New Rating ({books[book_id]['Rating']}): ") or books[book_id]['Rating']

            books[book_id].update({
                "Book Name": new_name,
                "Author": new_author,
                "Price": new_price,
                "Rating": new_rating
            })
            print("✅ Book updated successfully!\n")
        else:
            print("❌ Invalid Book ID.\n")
    except ValueError:
        print("⚠️ Invalid input.\n")


def delete_book():
    """Delete a book from the library"""
    view_books()
    try:
        book_id = int(input("Enter Book ID to delete: ")) - 1
        if 0 <= book_id < len(books):
            removed = books.pop(book_id)
            print(f"🗑️ Deleted: {removed['Book Name']} by {removed['Author']}\n")
        else:
            print("❌ Invalid Book ID.\n")
    except ValueError:
        print("⚠️ Invalid input.\n")


# Main Menu
while True:
    print("📖 Library Menu 📖")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        update_book()
    elif choice == "5":
        delete_book()
    elif choice == "6":
        print("👋 Exiting Library System. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.\n")
