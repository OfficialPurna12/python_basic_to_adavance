print("🎉 Welcome to Multiple Choose ")

scores = 0

# Question 1 

print("\n What does HTML stand for?")
print("A ) High Text Markup Language")
print("B) Hyper Text Markup Language")
print("C) Hyperlinks Text Markup Language")
print("D) Home Tool Markup Language ")

answers = input(" Your answer (A/B/C/D)").strip().lower()

if answers == "b":
    print("✅ Correct ")
    scores +=1
else:
    print("❌ Wrong The correct answer is (B)")


# Question 2

print("\n Which tag is used to define a paragraph in HTML?")
print("A) <Para>")
print("B) <p>")
print("C) <pg>")
print("D) <Paragraph> ")
answers = input("Your answer (A/B/C/D)").strip().lower()
if answers == "b":
    print("✅ Correct ")
    scores += 1
else:
    print("❌ Wrong ! The correct answer is (B)")

#Question 3

print("\n What is the purpose of the <br> tag?")
print("A) Start a new paragraph")
print("B) Bold text")
print("C) Break line")
print("D) Create a list")

answers = input("Your answer (A/B/C/D)").strip().lower()

if answers == "c":
    print("✅ Correct ")
    scores += 1
else:
    print("❌ Wrong! Correct answer is (C)")


#Question 4

print("\n How do you add an image to a webpage?")
print("A) <img src=url>")
print("B) <src=url>")
print("C) <image=url>")
print("D) <media src=url>")

answers = input("Your answer (A/B/C/D)").strip().lower()

if answers == "a":
    print("✅ Correct")
    scores += 1
else:
    print("❌Wrong ! Correct answer is (A)")


    

print(f"\n Your final score is : {scores}/4 ")

if scores == 4:
    print("Excellent ")
elif scores == 3:
    print("Very Good")
elif scores == 2:
    print("Your bad luck try next time ")
else:
    print("You are fail ")