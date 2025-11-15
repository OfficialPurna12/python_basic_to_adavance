import tkinter as tk
from tkinter import messagebox

# Signup credentials
user_name = "Purna Khatri"
user_password = "Purna@#123"

# Function to validate login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == user_name and password == user_password:
        messagebox.showinfo("Login", "✅ Login Successful!")
    elif username != user_name and password == user_password:
        messagebox.showerror("Login", "❌ Username doesn't match. Please try again!")
    elif username == user_name and password != user_password:
        messagebox.showerror("Login", "❌ Password doesn't match. Please write correct password!")
    else:
        messagebox.showerror("Login", "❌ Username and Password don't match. Please try again!")

# GUI window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Username label & entry
tk.Label(root, text="Username:").pack(pady=9)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password label & entry
tk.Label(root, text="Password:").pack(pady=9)
entry_password = tk.Entry(root , show="*")  # hides password
entry_password.pack(pady=5)

# Login button
tk.Button(root, text="Login", command=validate_login).pack(pady=10)

root.mainloop()
