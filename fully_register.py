import re
from datetime import datetime

# --- Registration Section ---
full_name = input("Please enter your name: ")

# --- Email validation ---
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
while True:
    email = input("Please enter your email: ")
    if re.match(email_pattern, email):
        break
    else:
        print("❌ Invalid email format! Example: example@gmail.com")

# --- Phone validation ---
while True:
    phone = input("Please enter your phone number: ")
    if phone.isdigit() and len(phone) == 10:
        break
    else:
        print("❌ Invalid phone number! Must be 10 digits.")

# --- Address ---
while True:
    address = input("Please enter your address: ")
    if address.strip():
        break
    else:
        print("❌ Address cannot be empty!")

# --- Father name ---
while True:
    father_name = input("Please enter your father's name: ")
    if father_name.strip():
        break
    else:
        print("❌ Father's name cannot be empty!")

# --- Mother name ---
while True:
    mother_name = input("Please enter your mother's name: ")
    if mother_name.strip():
        break
    else:
        print("❌ Mother's name cannot be empty!")

# --- Nationality ---
while True:
    nationality = input("Please enter your nationality: ").strip()
    if nationality:
        break
    else:
        print("❌ Nationality cannot be empty!")

# --- Date of Birth validation ---
while True:
    Date_of_Birth = input("Please enter your date of birth (DD/MM/YYYY): ")
    try:
        datetime.strptime(Date_of_Birth, "%d/%m/%Y")
        break
    except ValueError:
        print("❌ Invalid date! Please use format DD/MM/YYYY")

# --- Faculty ---
while True:
    faculty = input("Please enter your faculty: ").strip()
    if faculty:
        break
    else:
        print("❌ Faculty cannot be empty!")

# --- Password confirmation ---
while True:
    password = input("Please enter your password: ")
    confirm_password = input("Re-enter your password: ")

    if password == confirm_password:
        print("✅ Registration successful!")
        break
    else:
        print("❌ Passwords do not match! Please try again.")

# --- Store data into dictionary ---
user_data = {
    "full_name": full_name,
    "email": email,
    "phone": phone,
    "address": address,
    "father_name": father_name,
    "mother_name": mother_name,
    "nationality": nationality,
    "Date_of_Birth": Date_of_Birth,
    "faculty": faculty,
    "password": password
}

# --- Login Section ---
print("\n=== Welcome to the Login Page ===\n")

user_email = input("Please enter your email: ")
user_password = input("Please enter your password: ")

if user_email == user_data["email"] and user_password == user_data["password"]:
    print("🎉 Login successful!")
    print(f"Welcome, {user_data['full_name']} ❤️")
else:
    print("❌ Invalid email or password! Please register first.")
