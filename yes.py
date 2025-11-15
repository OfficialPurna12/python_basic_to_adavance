# Multiplication Table Program
print("📘 Multiplication Table Generator 📘")
print("-------------------------------------")

# Take input from the user
start = int(input("Enter the starting table number: "))
end = int(input("Enter the ending table number: "))

print("\n🧮 Multiplication Tables from", start, "to", end)
print("-------------------------------------\n")

# Loop through each table number
for i in range(start, end + 1):
    print(f"\n📄 Table of {i}")
    print("----------------")
    for j in range(1, 11):  # 1 to 10
        print(f"{i} x {j} = {i * j}")
    print("----------------")
