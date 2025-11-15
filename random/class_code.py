class Names:
    def __init__(self, full_name, email, phone_number, address, website):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.website = website

    def show_name(self):
        print("\n------ Personal Information ------")
        print(f"Full Name   : {self.full_name}")
        print(f"Email       : {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address     : {self.address}")
        print(f"Website     : {self.website}")
        print("----------------------------------")


# ---- User Input Section ----
full_name = input("Enter your full name: ")
email = input("Enter your email address: ")
phone_number = input("Enter your phone number: ")
address = input("Enter your address: ")
website = input("Enter your website: ")

# ---- Create Object ----
persona_one = Names(full_name, email, phone_number, address, website)

# ---- Display Information ----
persona_one.show_name()
