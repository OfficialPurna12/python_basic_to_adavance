print("🎉🎉 Welcome to our online quiz exam!")

score = 0

# Question 1
answer = input("What is the capital city of Nepal: ").strip().lower()
if answer == "kathmandu":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is: Kathmandu.")

# Question 2
answer = input("HTML stands for: ").strip().lower()
if answer == "hyper text markup language":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is: Hyper Text Markup Language.")

# Question 3
answer = input("CSS stands for: ").strip().lower()
if answer == "cascading style sheets":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is: Cascading Style Sheets.")

# Question 4
answer = input("JS stands for: ").strip().lower()
if answer == "javascript":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is: JavaScript.")

# Final Score
print(f"\nYour final score is: {score}/4")

if score == 4:
    print("🌟 Excellent! You got all correct!")
elif score >= 3:
    print("👍 Good job! Keep learning.")
else:
    print("💡 You can do better next time.")
