from pymongo import MongoClient
import getpass

client = MongoClient("mongodb://localhost:27017/")
db = client["user_system"]
user_collection = db["users"]

def signup():
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if user_collection.find_one({"username": username}):
        print("Username already exists!")
        return
    if user_collection.find_one({"email": email}):
        print("Email already exists!")
        return

    user_collection.insert_one({
        "username": username,
        "email": email,
        "password": password
    })
    print("Signup successful!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    user = user_collection.find_one({"username": username, "password": password})
    if user:
        print(f"Welcome {user['username']}! You are logged in.")
    else:
        print("Invalid username or password.")

while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
