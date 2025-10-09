# Write a function greet(name) that takes a person’s name and prints "Hello, <name>!" .
def greet(name):
    print(f"Hello,{name}!")

name = input("Enter your name:")
greet(name)

# Create a function add_numbers(a, b) that returns the sum of two numbers.
def add_numbers(a, b):
    return a + b

num_1 = int(input("Enter First number:"))
num_2 = int(input("Enter Second number:"))

result = add_numbers(num_1, num_2)
print(f"The sum is : {result}.")

# Define a function is_even(num) that returns True if the number is even, otherwise
# False .
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number:"))
Result1 = isEven(num)
if Result1:
    print(f"{Result1}. It is Even.")
else:
    print(f"{Result1}. It is Odd.")

# Write a function factorial(n) that returns the factorial of a given number using a
# loop.
def factorial(n):
    fact = 1 
    for i in range(1,n+1):
        fact *= i
    return fact

number = int(input("Enter a number:"))
Result2 = factorial(number)
print(f"The factorial of {number} is {Result2}")

# Create a function convert_to_celsius(fahrenheit) that converts Fahrenheit to Celsius.
def convertToCelsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

fahrenheit = int(input("Enter the Reading of Fahrenheit:"))
Result3 = round(convertToCelsius(fahrenheit), 2)
print(f"The Reading of Fahrenheit {fahrenheit} is {Result3} Celsius")

# Part B – Parameters & Return (5 Questions)
# 1. Write a function calculate_area(length, width=5) that calculates the area of a rectangle (use default argument for width).
def calculateArea(length, width = 5):
    area = length * width
    return area
length = int(input("Enter the lenght of the rectangle:"))
print("Default value of width is taken which is 5.")
ResultArea = calculateArea(length)
print(f"Hence , the area of the rectangle is {ResultArea}")

# 2. Define a function power(base, exponent=2) that returns base raised to the power of exponent (default square).
def exponentiation(base, exponent = 2):
    return base ** exponent

base = int(input("Enter the Base:"))
print("THe exponent is taken default value which is 2.")
ResultExponent = exponentiation(base)
print(f"Hence , the base raised to the power of exponent is {ResultExponent}")

# 3. Write a function count_vowels(word) that returns the number of vowels in a string.
def countVowels(word):
    vowel = "aeiou"
    count = 0
    for char in word.lower():
        if char in vowel:
            count += 1
    print(f"The number of vowels in the word {word} is {count}")

word = input("Enter a word:")
countVowels(word)

# 4. Create a function reverse_string(s) that returns the reversed version of the string.
def reverseString(string):
    return string[-1::-1]

string = input("Enter a word:")
ProcessedString = reverseString(string)
print(f"The reversed version of the string {string} is {ProcessedString}")

# 5. Write a function max_of_three(a, b, c) that returns the largest of three numbers.
def maxOfThree(a, b, c):
    if a < b  and c < b:
        return b
    elif b < a and c < a:
        return a
    else:
        return c

output = maxOfThree(11,87,90)
print(f"{output} is greatest.")
