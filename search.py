

# find the negative and positive number using user interface


# num = float(input("Enter the number :  "))

# if num >0:
#     print("The number is positive ")
# elif num < 0:
#     print("The number is negative ")
# else:
#     print("The umber is zero ")


#  Age check 


age = int(input("Enter your age : "))


# Program to check age category

# Take input from the user
age = int(input("Enter your age: "))

# Check age categories
if age < 0:
    print("❌ Invalid age. Please enter a valid number.")
elif age <= 12:
    print("👶 You are a Child.")
elif age <= 19:
    print("🧑 You are a Teenager.")
elif age <= 59:
    print("👨 You are an Adult.")
else:
    print("👴 You are a Senior.")
