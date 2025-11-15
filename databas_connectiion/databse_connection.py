import mysql.connector
from mysql.connector import Error
import getpass  # hides password input

# MySQL connection
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",        # your MySQL username
            password="",        # your MySQL password
            database="user_system"
        )
        return conn
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None

# Signup function
def signup():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = getpass.getpass("Enter password: ")

        try:
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)
            )
            conn.commit()
            print("Signup successful!")
        except Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

# Login function
def login():
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cursor.fetchone()
        if user:
            print(f"Welcome {user[1]}! You are logged in.")
        else:
            print("Invalid username or password.")
        cursor.close()
        conn.close()

# Main program
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
        print("Invalid choice. Try again.")
