import random
# Convert a float to an integer (and observe truncation).
# Convert a string "25.5" to a float and add 10 to it.

newFloat = 13.0987
print(f"Value: {newFloat}, Type: {type(newFloat)}")

print("Performing the explicit type cast to change into integer")
newInt = int(newFloat)
print(f"Value: {newInt}, Type: {type(newInt)}")

inputNum = input ("Enter a number: ")
print(f"Value: {inputNum}, Type: {type(inputNum)}")

castinput = float(inputNum)
print("Changing the type of input from string to float and adding 10 to it")
print(f"Value: {castinput} added 10 {castinput + 10}, Type: {type(castinput + 10)}")

# Use max() and min() to find the largest and smallest of three numbers.
# Use sum() to add a list of integers

numList = [25,51,9]
print(f'max value in the list {numList} is: {max(numList)}')
print(f'min value in the list {numList} is: {min(numList)}')
print(f'sum of all values in the list {numList} is: {sum(numList)}')

# Generate a random integer between 1 and 100 (use random.randint() ).
randomInt = random.randint(1,100)
print(f'Random integer between 1 and 100 is: {randomInt}')
