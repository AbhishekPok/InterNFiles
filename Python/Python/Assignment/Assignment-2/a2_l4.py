import math
# Create a program to check if a number is even or odd.
def check_even_odd(number):
    """check either the number is even or odd"""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

numb = int(input("Enter a number: " ))
result = check_even_odd(numb)
print(f"The number {numb} is {result}.")

def calculate_SI(principal, rate, time):
    """Calculate Simple Interest"""
    return (principal * rate * time) / 100

# Calculate the simple interest for a given principal, rate, and time.
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))
si = calculate_SI(p, r, t)
print(f"The Simple Interest for principal {p}, rate {r}%, time {t} years is: {si}")

# Convert seconds into hours, minutes, and seconds format.
def convert_Seconds(total_seconds):
    """Convert seconds to hours, minutes, and seconds"""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

total_seconds = int(input("Enter the total seconds: "))
hours, minutes, seconds = convert_Seconds(total_seconds)
print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")

# Find the Distance between two points [x1,y1] and [x2,y2]

a , b = map(int,input("Enter the value of points (x1,y1):").split(" "))
c , d = map(int,input("Enter the value of points (x2,y2):").split(" "))

distance = math.sqrt((c-a)**2 + (d-b)**2)

print(f"The distance between points ({a},{b}) and ({c},{d}) is: {abs(distance)}")


