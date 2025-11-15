print("🎉 Welcome to my official online quiz game!!")

score = 0  # corrected variable name from 'scores' for clarity

# Question 1
print("\n1️⃣ What does HTML stand for?")
print("A) Hyper Trainer Marking Language")
print("B) Hyper Text Markup Language")
print("C) Hyper Text Marketing Language")
print("D) Hyperlink and Text Markup Language")

answer = input("Your answer is (A/B/C/D): ").strip().upper()

if answer == "B":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is: B) Hyper Text Markup Language")

# Question 2
print("\n2️⃣ Which HTML5 element is used to play video files?")
print("A) <media>")
print("B) <movie>")
print("C) <video>")
print("D) <player>")

answer = input("Your answer is (A/B/C/D): ").strip().upper()

if answer == "C":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is: C) <video>")

# Question 3
print("\n3️⃣ Which tag is used to draw graphics in HTML5?")
print("A) <canvas>")
print("B) <graphic>")
print("C) <svg>")
print("D) <draw>")

answer = input("Your answer is (A/B/C/D): ").strip().upper()

if answer == "A":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is: A) <canvas>")

# Question 4
print("\n4️⃣ Which HTML5 element defines navigation links?")
print("A) <navigate>")
print("B) <nav>")
print("C) <menu>")
print("D) <links>")

answer = input("Your answer is (A/B/C/D): ").strip().upper()

if answer == "B":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is: B) <nav>")

# Final Score
print(f"\n🎯 Your Final Score is: {score}/4")

if score == 4:
    print("🌟 Excellent!")
elif score >= 3:
    print("👍 Good job!")
else:
    print("💪 You can do better next time — keep learning!")
