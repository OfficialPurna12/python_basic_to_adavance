

#  Signup page


user_name = "Purna Khatri"
user_password = "Purna@#123"



#  User interface 

username = input("Enter your username : ")
password = input("Enter your password : ")

#  Validation 


if user_name == username and user_password == password:
    print(f"✅ Login Successfully !" )

elif user_name != username and user_password == password:
    print("❌ Username does't match please try again !")

elif user_name == username and user_password != password:
    print("❌ Password doesn't match please write  correct password !")

else:
    print("Username and password doesn't match please try again ")