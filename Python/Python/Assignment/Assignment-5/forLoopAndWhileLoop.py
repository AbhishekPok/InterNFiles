# Assignment for the Loop in Python
# Part 1 : Basics => For Loop

# Loop to Print numbers from 1 to 10
for _ in range(1,11):
    print(_)
print("-"*20)

# Loop to print even numbers from 1 to 50
for _ in range(0,51,2):
    print(_, end=" ")
print("")
print("-"*20)

#Loop to print the Multiplication table 
for a in range(1,11):
        output = a * 5
        print(f"{5} x {a} = {output}")
print("=============================")

# mizash = 100, 

# Write a program to calculate the sum of first 100 natural numbers.
num = 0
for _ in range(1,101):
    num += _
print(f"The sum of first 100 natural numbers is: {num}")

# Print each character of a string "Python" using a for loop.
string = "Python"
for char in string:
    print(char,end=" ")
print("\n")

# Part 2 : Basic => While Loop
# Write a program to print numbers from 1 to 10 using a while loop.
count = 1
while count <= 10:
    print(count)
    count += 1

# Keep asking the user for a number until they enter 0 (then stop).
enter = int(input("Enter a number:"))
while enter != 0:
    print(f"The number you've enter is not \"0\" but {enter}")
    print("Entering into the Loop.")
    enter = int(input("Enter a number:"))
print(f"The number entered is {enter}, exiting the Loop.")

# Write a program that prints numbers 10 down to 1 using a while loop.
a = 10
while a > 0:
    print(a)
    a -= 1

# Create a program that keeps asking for a password until the correct one
# ( "Python123" ) is entered.
password = input("Enter the password:")
while password != "Python123":
    print("Password Incorrect. Entering into the Loop.\nPlease Enter the correct password to exit the Loop.")
    password = input("Enter the password:")
print("Password Correct. Exiting the Loop.")

# Write a program that keeps rolling a dice (random 1–6) until it rolls a 6
import random

while True:
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        print(f"The dice rolled out {dice}.")
        break

# Part 3: Loop Control (break, continue, pass)
# 1. Print numbers from 1 to 20, but skip multiples of 5.
for _ in range (1,21):
    if _ % 5 == 0:
        continue
    print(_)

# Ask the user to enter numbers. Stop when they enter a negative number, then
# print the sum of all entered positive numbers.
calc = []
while True:
    num = int(input("Enter a number:"))
    if num >= 0:
        calc.append(num)
    else:
        break
sumation = sum(calc)
print(f"The sum of all entered positive numbers is {sumation}")

# Write a program that checks if a number is prime (use a loop)

num = int(input("Enter a number:"))
for _ in range(2,num):
     if num % _ == 0:
         print(f"The number {num} is not a prime number.")
         break
     else:
         print(f"The number {num} is a prime number.")
         break

# Print the first 10 Fibonacci numbers using a loop.
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b

# Write a program that finds the factorial of a number using a loop.
num = int(input("Enter a number:"))
fact = []
for _ in range(1,num + 1):
     if num % _ == 0:
        fact.append(_)

print(f"The factorial of {num} is {fact}")

# Part 4: Nested Loops
# 1. Print a square pattern of stars () with size 5x5 .
for row in range(1,6):
    for col in range(1,6):
        print("*",end = "")
    print("")

# . Print a right-angled triangle of stars with 5 rows
for row in range(1,6):
    for col in range(0,row):
        print("*",end = "")
    print("")

# Print a multiplication table (1 to 10) in grid format.
# number  = int(input("Enter a number:"))
for a in range(1,11):
    for b in range(1,11):
        output = a * b
        print(f"{a} x {b} = {output}")
    print("=============================")

# Write a program that prints all pairs (i, j) where i and j are numbers from 1 to 3 .

for i in range(1,4):
    for j in range(1,4):
        print(f"({i},{j})")

# Create a number pyramid like this (for n=5 ):

for i in range(1,6):
    for j in range(1,i + 1):
        print(j, end = "")
    print("")

# Part 5: Real-Life Scenarios
# 1. Simulate a bank account system:
# Start with balance = 1000 .
# Keep asking deposit/withdraw until user types "exit" .
# Update balance after each operation.

balance = 1000
while True:
    print("1. Deposit")
    print("2. WithDraw")
    print("3. Exit")
    choice = int(input("Enter your choice:"))
    print(f"Balance Status:{balance}")
    if choice == 1:
        print("You've chosen to Deposit.")
        amount = int(input("Enter the amount:"))
        balance += amount
        print(f"Balance Status:{balance}")
    elif choice == 2:
        print("You've chosen to WithDraw.")
        amount = int(input("Enter the amount:"))
        balance -= amount
        print(f"Balance Status:{balance}")
    elif choice == 3:
        print("You've chosen to Exit.")
        break
    else:
        print("Invalid Choice.Please Enter a valid choice provided below.(1-3)")

# . Write a guessing game:
# Computer picks a random number (1–20).
# User keeps guessing until correct.
# Give hints "Too High" / "Too Low" .
num = random.randint(1,20)
while True:
    guess = int(input("Enter your guess:"))
    if guess > num:
        print("Too High")
    elif guess < num:
        print("Too Low")
    elif guess == num:
        print("You've guessed it!")
        break

# Write a program that counts how many vowels are in a string.
string = input("Enter a string:")
vowel = []
count = 0
vowels = "aeiou"
for char in string.lower():
    if char in vowels:
        count += 1
        vowel.append(char)
print(f"The number of vowels in the string is {count} and the vowels are {set(vowel)}")

# Create a simple ATM PIN system:
# User gets max 3 attempts.
# If PIN is correct → "Access Granted" .
# If wrong 3 times → "Card Blocked" .

pin = "2456"
attempt = 0
while True:
    askUser = int(input("Enter your PIN:"))
    if askUser == int(pin):
        print("Access Granted")
        break
    else:
        print(f"Wrong PIN. You have {2-attempt} attempts left.")
        attempt +=1
        if attempt == 3:
            print("Card Blocked")
            break

# Write a program that reads a list of numbers and finds the largest and
# smallest number using a loop (don’t use max / min ).
checklist = [10,25,44,87,62,75,32]
# newchecklist = sorted(checklist) #can't use the sorted function, use loop to sort the list and display the [0] index for smallest and [-1] index for largest.
# print(newchecklist)
def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

listSize = len(checklist)
selectionSort(checklist,listSize)
print(f"The smallest number in the list is {checklist[0]} and the largest number in the list is {checklist[-1]}")

#############################################
# Part 6: Challenges (For Extra Practice 🚀)#
#############################################

# 1. Print a diamond pattern of stars (n=5).
#   *
#  ***
# *****
#  ***
#   * 
def print_diamond(n):
    if n % 2 == 0:
        print("The value must be an even number.")
    mid = n // 2

    # top half (including middle row)
    for i in range(mid + 1):
        stars = 2 * i + 1
        spaces = (n - stars) // 2
        print(' ' * spaces + '*' * stars)

    # bottom half
    for i in range(mid - 1, -1, -1):
        stars = 2 * i + 1
        spaces = (n - stars) // 2
        print(' ' * spaces + '*' * stars)

# Example:
print_diamond(5)
primeList = []
# Generate the first 20 prime numbers using a loop
def generatePrimes(limit):
    for num in range(2, limit + 1):  
        for n in range(2, num):     
            if num % n == 0:
                break
        else:
            primeList.append(num)    

generatePrimes(20)
print(primeList)

# Build a rock-paper-scissors game using loops (play until user types "quit" ).
import random

while True:
    computerChoice = random.choice(["rock","scissors","paper"])
    userChoice = input("Enter Rock,Scissors or Paper:")
    if userChoice.lower() == "quit":
        break
    elif userChoice.lower() == computerChoice:
        print("It's a tie")
    elif (userChoice.lower() == "rock" and computerChoice == "scissors") or \
         (userChoice.lower() == "paper" and computerChoice == "rock") or \
         (userChoice.lower() == "scissors" and computerChoice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Create a basic calculator that keeps running until user types "exit" .

while True:
    print("Enter two numbers with an operator in between:")
    num1 = float(input("Enter first number:"))
    operator = input("Enter operator:")
    num2 = float(input("Enter second number:"))
    if operator == "+":
        print(num1 + num2)
        exit = input("Continue? y/n ")
        if exit == "n":
            break
    elif operator == "-":
        print(num1 - num2)
        exit = input("Continue? y/n ")
        if exit == "n":
            break
    elif operator == "*":
        print(num1 * num2)
        exit = input("Continue? y/n ")    
        if exit == "n":
            break    
    elif operator == "/":
        print(num1 / num2)
        exit = input("Continue? y/n ")
        if exit == "n":
            break


# Write a program to simulate a snake game counter:
# Start at score 0.
# Every loop, randomly decide if the snake eats food → +10 points.
# Stop the game when score reaches 100.
import random
n = 0
while n < 100:
    score = random.choice([0,1])
    if score == 1:
        print("Snake Ate the Apple.")
        n += 10
        print("score:",n)
    else:
        print("Snake Didn't Ate the Apple.")
        n += 0

