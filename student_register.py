students = {
    "Purna Bahadur Khatri": [71, 77, 85, 80],
    "Dammar Khanal": [68, 88, 73, 74],
    "Nabin Nath": [88, 67, 71, 76],
    "Gambhir Jaisi": [88, 82, 81, 71]
}

print("📓 Student Grade Report")
# print("=" * 50)

for name, marks in students.items():
    total = sum(marks)
    average = total / len(marks)

    # Grade calculation inside the loop 👇
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    # Print each student’s report
    print(f"\nName     : {name}")
    print(f"Marks    : {marks}")
    print(f"Total    : {total}")
    print(f"Average  : {average:.2f}")
    print(f"Grade    : {grade}")
    # print("-" * 50)
