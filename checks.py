number_one = input("Enter the first number : ")
number_two = input("Enter the second number : ")


if number_one > number_two:
    print(f"Largest number is : {number_one}")
    print(f"Small number is : {number_two}")

elif number_two > number_one:
    print(f"Larger number : {number_two}")
    print(f"Small number is : {number_one}")

else:
    print(f"Both number are equal : {number_one}")