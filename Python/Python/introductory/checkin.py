#use of in : output in boolean
# a = [1, 2, 3, 4, 5]   
# print(3 in a)  # True 
# print(6 in a)  # False    
name = "Abhishek"
age = 24
statement = f"My name is {name} and I am {age} years old"
word = "name"
output = word in statement
output2 = "hello" in statement
print(f"word in statement => {output}")  # True
print(f"hello in statement => {output2}")  # False
