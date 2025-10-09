# Assignment: Conditionals and Booleans in Python

# ---------------- Part 1: Basics ----------------

# 1. Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("-" * 40)

# 2. Age category
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")

print("-" * 40)

# 3. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("-" * 40)

# 4. Password check
password = input("Enter password: ")
if password == "Python123":
    print("Access Granted")
else:
    print("Access Denied")

print("-" * 40)


# ---------------- Part 2: Booleans ----------------

# 1. Temperature check
temperature = int(input("Enter temperature: "))
if temperature > 30:
    print("It's hot")
else:
    print("It's normal")

print("-" * 40)

# 2. Raining and Umbrella
is_raining = True
has_umbrella = False
if is_raining and has_umbrella:
    print("You can go outside")
elif is_raining and not has_umbrella:
    print("Stay inside")

print("-" * 40)


# ---------------- Part 3: Elif and Nested ----------------

# 1. Grading system
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")

print("-" * 40)

# 2. Traffic light
light = input("Enter light color: ")
if light == "Red":
    print("Stop")
elif light == "Yellow":
    print("Get Ready")
elif light == "Green":
    print("Go")
else:
    print("Invalid light color")

print("-" * 40)

# 3. FizzBuzz
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

print("-" * 40)


# ---------------- Part 4: Real-Life Scenarios ----------------

# 1. ATM Simulation
balance = 5000
withdraw = int(input("Enter amount to withdraw: "))
if balance >= withdraw:
    print("Transaction successful")
else:
    print("Insufficient balance")

print("-" * 40)

# 2. Login System
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
elif username != "admin":
    print("Invalid username")
elif password != "1234":
    print("Invalid password")

print("-" * 40)

# 3. Eligibility check
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not eligible to Vote")

if age >= 16:
    print("Eligible to Drive")
else:
    print("Not eligible to Drive")

if age >= 21:
    print("Eligible to Drink")
else:
    print("Not eligible to Drink")

print("-" * 40)


# ---------------- Part 5: Challenge ----------------

# 1. Rock-Paper-Scissors
import random
user = input("Enter rock, paper, or scissors: ")
computer = random.choice(["rock", "paper", "scissors"])
print("Computer chose:", computer)
if user == computer:
    print("It's a tie")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")

print("-" * 40)

# 2. Quiz Game
score = 0
q1 = input("What is the capital of Nepal? ")
if q1.lower() == "kathmandu":
    score += 1
q2 = input("What is 5 + 5? ")
if q2 == "10":
    score += 1
q3 = input("What is the programming language we are learning? ")
if q3.lower() == "python":
    score += 1
print("Your total score is:", score)

print("-" * 40)
