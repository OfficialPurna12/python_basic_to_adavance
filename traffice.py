# Grade Sheet Program (without function)

# --- Input Section ---
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

# Enter marks for subjects with validation

try:
    eng = int(input("Enter marks in English: "))
    if eng < 0 or eng > 100:
        print("❌ Invalid marks in English! Enter between 0 and 100.")
        exit()

    math = int(input("Enter marks in Mathematics: "))
    if math < 0 or math > 100:
        print("❌ Invalid marks in Mathematics! Enter between 0 and 100.")
        exit()

    sci = int(input("Enter marks in Science: "))
    if sci < 0 or sci > 100:
        print("❌ Invalid marks in Science! Enter between 0 and 100.")
        exit()

    comp = int(input("Enter marks in Computer: "))
    if comp < 0 or comp > 100:
        print("❌ Invalid marks in Computer! Enter between 0 and 100.")
        exit()

    nep = int(input("Enter marks in Nepali: "))
    if nep < 0 or nep > 100:
        print("❌ Invalid marks in Nepali! Enter between 0 and 100.")
        exit()

except ValueError:
    print("Only accept number not accepted string")

# --- Calculation Section ---
total = eng + math + sci + comp + nep
percentage = total / 5

# Grade Calculation
if percentage >= 90 and percentage <= 100:
    grade = "A+ Excellent"
elif percentage >= 80:
    grade = "A Good"
elif percentage >= 70:
    grade = "B+ Very Good"
elif percentage >= 60:
    grade = "B Good"
elif percentage >= 50:
    grade = "C Needs Improvement"
elif percentage >= 40:
    grade = "D Poor"
else:
    grade = "F Fail"

# --- Output Section (Grade Sheet) ---
print("\n============== GRADE SHEET ==============")
print(f"Student Name : {name}")
print(f"Roll Number  : {roll}")
print("------------------------------------------")
print(f"English      : {eng}")
print(f"Mathematics  : {math}")
print(f"Science      : {sci}")
print(f"Computer     : {comp}")
print(f"Nepali       : {nep}")
print("------------------------------------------")
print(f"Total Marks  : {total}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
print("==========================================")
