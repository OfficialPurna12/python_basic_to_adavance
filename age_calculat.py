

from datetime import datetime

#  Current year
current_year = datetime.now().year

#  user input
birth_year = input("Enter your year od birth in format 'YYY' : ")

#  Calculate age 

age = current_year - int(birth_year)

print(f"You are {age} years old ")