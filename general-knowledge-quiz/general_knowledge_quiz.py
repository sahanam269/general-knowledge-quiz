print("===== GENERAL KNOWLEDGE QUIZ =====")

score = 0

# Question 1
print("\n1. What is the capital of France?")
answer = input("Your answer: ").strip().lower()

if answer == "paris":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
print("\n2. Which planet is known as the Red Planet?")
answer = input("Your answer: ").strip().lower()

if answer == "mars":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Question 3
print("\n3. How many days are there in a week?")
answer = input("Your answer: ").strip()

if answer == "7":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

# Final score
print("\n===== QUIZ COMPLETED =====")
print("Your final score is:", score, "/ 3")

if score == 3:
    print("Excellent! ")
elif score == 2:
    print("Good job! ")
elif score == 1:
    print("Keep practicing! ")
else:
    print("Try again and improve! ")