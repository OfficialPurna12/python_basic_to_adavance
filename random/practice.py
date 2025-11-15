class Name:
    
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def show_names(self):
        print(f"----Personal Information------ \n")
        print(f" Name : {self.name}")
        print(f" Phone : {self.phone}")
        print(f" Email : {self.email}")
        print(f" Address : {self.address}")

#  User input

name = input("Enter your full_name : ")
phone = input("Enter your phone Number : ")
email = input("Enter your Email : ")
address = input("Enter your Address : ")

person_one = Name(name, phone, email, address)

person_one.show_names()