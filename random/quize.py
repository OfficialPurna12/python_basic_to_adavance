print("🎉 Welcome to the Multiple-Choice Quiz Game!")
print("=" * 50)

score = 0

# Question 1
print("\n1️⃣ What is the capital city of Nepal?")
print("A) Pokhara")
print("B) Biratnagar")
print("C) Kathmandu")
print("D) Lalitpur")
answer = input("👉 Your answer (A/B/C/D): ").strip().lower()

if answer == "c":
    print("✅ Correct! Kathmandu is the capital city of Nepal.")
    score += 1
else:
    print("❌ Wrong! The correct answer is C) Kathmandu.")

# Question 2
print("\n2️⃣ HTML stands for:")
print("A) HighText Machine Language")
print("B) HyperText and Links Markup Language")
print("C) Hyper Text Markup Language")
print("D) Home Tool Markup Language")
answer = input("👉 Your answer (A/B/C/D): ").strip().lower()

if answer == "c":
    print("✅ Correct! HTML stands for Hyper Text Markup Language.")
    score += 1
else:
    print("❌ Wrong! The correct answer is C) Hyper Text Markup Language.")

# Question 3
print("\n3️⃣ CSS stands for:")
print("A) Colorful Style Sheets")
print("B) Creative Style System")
print("C) Cascading Style Sheets")     
print("D) Computer Style System")
answer = input("👉 Your answer (A/B/C/D): ").strip().lower()

if answer == "c":
    print("✅ Correct! CSS stands for Cascading Style Sheets.")
    score += 1
else:
    print("❌ Wrong! The correct answer is C) Cascading Style Sheets.")

# Question 4
print("\n4️⃣ JS stands for:")
print("A) JavaSystem")
print("B) JavaScript")
print("C) JustScript")
print("D) JScript")
answer = input("👉 Your answer (A/B/C/D): ").strip().lower()

if answer == "b":
    print("✅ Correct! JS stands for JavaScript.")
    score += 1
else:
    print("❌ Wrong! The correct answer is B) JavaScript.")

# Final Score
print("\n" + "=" * 50)
print(f"🏁 Your final score is: {score}/4")

if score == 4:
    print("🌟 Excellent! You got all correct!")
elif score >= 2:
    print("👍 Good job! Keep learning.")
else:
    print("💡 You can do better next time.")
