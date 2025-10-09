#Level 1 – Basics (Warm-Up)
# Store your age in a variable and print it.
# Store the price of an item (float) and print it.
# Add, subtract, multiply, and divide two integers.
# Divide two integers and show:
# Normal division ( / )
# Floor division ( // )
# Modulus ( % )
# Multiply a float by an integer and print the result.
# Use type() to check the data type of each result

def printdetails(newList):
    for operation in newList:
        print(f"Type of {operation} is {type(operation)}")
        
age = 22
price = 1910.56
print(f"Age: {age}, Type: {type(age)}")
print(f"Price: {price}, Type: {type(price)}")

add = age + price
sub = price - age
prod = age * price
normDiv = price / age


print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {prod}")
print(f"Normal Division: {normDiv}")

newList = [add, sub, prod, normDiv]
printdetails(newList)

#Division types like normal division, Floor Division and Modulus
floorDiv = price // age
Remainder = price % age #using modulus operator

print(f"Floor Division: {floorDiv}")
print(f"Remainder using modulus operator: {Remainder}")

list2 = [floorDiv, Remainder]
printdetails(list2)


