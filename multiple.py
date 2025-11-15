

#  Multiple table

print("Multiple Table Generation \n")

#  Take input from the user

first_number = int(input("Enter the required table first_number :  "))
second_number  = int(input("Enter the required table second_number : "))


print(f" Multiplication Tables from , {first_number} to {second_number}")


#  use of for loop 

for a in range(first_number, second_number + 1):
    print(f"Table of {a}")

    for j in range(1,11):
        print(f" {a} x {j} = {a * j}")