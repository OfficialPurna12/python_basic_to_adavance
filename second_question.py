
def record_user_data():
   
    print("Enter your details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")

    # Data format
    user_data = f"First Name: {first_name}, Last Name: {last_name}, Email: {email}, Phone: {phone}\n"

    # Save to file
    with open("user_info.txt", "a") as file:
        file.write(user_data)

    print("✅ Your data has been recorded.\n")


def show_user_data():
   
    print("📄 Saved User Data:")
    try:
        with open("user_info.txt", "r") as file:
            data = file.read()
            if data.strip():
                print(data)
            else:
                print("No user data found.")
    except FileNotFoundError:
        print("No data file found. Please record some user data first.\n")




    while True:
        print("\nChoose an option:")
        print("1. Record new user data")
        print("2. Show all user data")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            record_user_data()
        elif choice == "2":
            show_user_data()
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
  record_user_data()