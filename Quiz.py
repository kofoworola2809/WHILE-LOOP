score = 0

print("🧠 Python Data Structure Quiz Game 🧠")
print("Choose the correct answer (a, b, c, or d)\n")

# Question 1
print("1. Which brackets are used for a list?")
print("a) ()  b) []  c) {}  d) <>")
answer = input("Your answer: ").lower()
if answer == "b":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is b) []")

# Question 2
print("\n2. What is a tuple?")
print("a) A changeable group of items")
print("b) An ordered, unchangeable collection")
print("c) A list with no duplicates")
print("d) A key-value pair")
answer = input("Your answer: ").lower()
if answer == "b":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is b) An ordered, unchangeable collection")

# Question 3
print("\n3. What makes a set unique?")
print("a) It keeps items in order")
print("b) It allows duplicates")
print("c) It only stores key-value pairs")
print("d) It removes duplicates automatically")
answer = input("Your answer: ").lower()
if answer == "d":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is d) It removes duplicates automatically")

# Question 4
print("\n4. How do you define a dictionary?")
print("a) []  b) ()  c) {} with key: value  d) {} with numbers only")
answer = input("Your answer: ").lower()
if answer == "c":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is c) {} with key: value")

# Question 5
print("\n5. What will this code return: len({1, 2, 2, 3})")
print("a) 4  b) 3  c) 2  d) Error")
answer = input("Your answer: ").lower()
if answer == "b":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is b) 3")

# Final Score
print(f"\n🎯 Quiz finished! Your score is {score}/5")

if score == 5:
    print("🔥 You nailed it! Python pro!")
elif score >= 3:
    print("👍 Good job! You're getting there!")
else:
    print("📚 Keep practicing, you’ve got this!")