import random
#username generation in the format: firstname.lastnameYY , where YY are the last two digits of the year of birth.
#task 1
first_name = (input("Enter your first name: "))
last_name = (input("Enter your last name: "))
DOB = (input("Enter your date of birth (DD/MM/YYYY): "))
username = (f"{first_name.lower()}.{last_name.lower()}{DOB[-2:]}")
print(f"Your username is: {username}")
#task 2
text = input("Enter a string: ")
reverse = text[-1::-1]
random_int = random.randint(0,50)
print(f"Password generated: {reverse.upper()}{random_int}")
# task 3
text2 = input("Enter another string: ")
for word in text2.split():
    print(f"{word[1:]}{word[0]}ay", end = " ")
print()