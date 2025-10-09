# Create a set with the values {1, 2, 3, 4, 5} and print it.
set1 = {1,2,3,4,5}
print(f"THe created set is as follow:\n{set1}")

# Create an empty set and verify its type.
empty_Set = set()
print(f"The empty set is as follow:\n{empty_Set} type = {type(empty_Set)}")

# 3. Add an element "python" to a set.
empty_Set.add("Python")
print(f"Element added as follow:\n{empty_Set}")

# Remove an element from a set using both .remove() and .discard() and observe
# the difference.

#  empty_Set.remove("Apple") # <- uncomment after the completion of the assigment
# Output : Exception faced as follows :-
# Traceback (most recent call last):
#   File "/home/abhishek/Documents/PythonIntern/Assignment/Assignment-3/set_assignment.py", line 16, in <module>
#     empty_Set.remove("Apple")
#     ~~~~~~~~~~~~~~~~^^^^^^^^^
# KeyError: 'Apple'.
# Program terminated .
# empty_Set.discard("Apple")
# Output : No exception faced.

# Check if 10 exists in {5, 10, 15, 20} .
newSet = {5, 10, 15, 20}
check = 10 in newSet
if check:
    print(f"There is \'10\' in the set{newSet}.")

# Operation in Set 
# . Find the union of {1, 2, 3} and {3, 4, 5} .
operationSet1 = {1,2,3}
operationSet2 = {3,4,5}
Union = operationSet1 | operationSet2
print(f"The union of the sets {operationSet1} and {operationSet2} is {Union}")

# Find the intersection of {10, 20, 30} and {20, 40, 60} .

operationSet3 = {10, 20, 30} 
operationSet4 = {20, 40, 60}
Intersection = operationSet3 & operationSet4
print(f"The intersection of the sets {operationSet3} and {operationSet4} is {Intersection}")

# Find the difference between {1, 2, 3, 4} and {3, 4, 5, 6} .

operationSet5 = {1, 2, 3, 4}
operationSet6 = {3, 4, 5, 6}
Difference = operationSet5 - operationSet6
print(f"The Difference of the sets {operationSet5} and {operationSet6} is {Difference}")

#Creating set of String  

exampleString = "Abhishek"
strSet = set(exampleString)
print(f"The string is {exampleString} and the set created from the string is {strSet}.")

# Remove duplicates from a list using a set.

exampleList = ["Abhishek","Saugat","Abhishek","Abhisha","Nabina","Shridhi"]
setFromExampleList = set(exampleList)
print(f"Created a set to remove the Duplicated Element in the {exampleList}:{setFromExampleList}")
print(f"Converted the set back to list.")
newlist = list(setFromExampleList)
print(f"{newlist}")

# Challenging
# 1. Given two sets, check if one is a subset of the other.

setA = {'a','b','c','d','e','f','g','h','i','j'}
setB = {'a','e','i'}
print(f"The considered sets are:\nA:{setA}\nB:{setB}.")
print(f"checking if set A is subset of set B :{setA.issubset(setB)} \nIs set B is the subset of set A:{setB.issubset(setA)}")

# Write a program to find elements that are in either of two sets but not in both
setB = {'a','e','i','o','u'}
semanticOperation = setA ^ setB
print(f"elements that are in either of two sets i.e \nA:{setA}\nB:{setB}\nbut not in both:{semanticOperation}")

# Use set comprehension to create a set of squares from 1 to 10.
setSquare = {x * x for x in range(1, 11)}
print(f"The set of squares from 1 to 10 :{setSquare}")

# Given a sentence, find all unique words using a set
sentence = input("Enter About Yourself:\n")
setFromInput = sentence.split(" ")
setification = set(setFromInput)
print(f"All unique words are:{setification}")

# Write a program that checks if two strings are anagrams using sets.
string1 = input("Enter the first string:")
string2 = input("Enter the second string:")

# accurate result
if sorted(string1.lower()) == sorted(string2.lower()):
    print("These 2 sentences are anagram.")
else:
    print("These 2 sentences arenot anagram.")
#using set
checkSet1 = set(string1.lower())
checkSet2 = set(string2.lower())
if checkSet1 == checkSet2:
    print("These 2 sentences are anagram.")
else:
    print("These 2 sentences arenot anagram.")

# Mixed Tuple and Set

# 1. Create a tuple of numbers, convert it to a set, and then back to a tuple.
newTuple = (1,2,3,4,5,6,7,7,8,8,8,9,9,9,9)
setConversion = set(newTuple)
print(f"Initial of the Tuple:\n{newTuple}\nConverted to set as: {setConversion}")
print(f"Conveted Back to tuple as {tuple(setConversion)}")

# 2. Given a list with duplicates, convert it to a tuple with only unique values.
MixedExampleList = [1,2,3,4,5,6,7,7,8,8,8,9,9,9,9]
listConversion = set(MixedExampleList)
tupleFromCOnversion = tuple(listConversion)
print(f"Initial List:\n{MixedExampleList}\nConversion to set:{listConversion}\nCreating the Tuple from the set:{tupleFromCOnversion}")

# Given t = (1, 2, 3, 2, 4, 1) , find all unique elements and store them in a set.

t = (1, 2, 3, 2, 4, 1)
setT = set(t)
print(f"Initial tuple{t}\nStoring into set{setT}")

# Store 5 tuples (name, age) in a set and display all people older than 25.
setOfTuple = {('Abhishek',22),('Saugat',21),('Shridhi',25),('Abhisha',26),('Sachet',26)}
for name,age in setOfTuple:
    if age >= 25:
        print(f"{name}-{age}")

# Find common elements between two tuples using sets.

newTuple # from line 108
t # from line 121

intersectionTuple = tuple(set(newTuple) & set(t))
print(f"The common element between two tuples are:{intersectionTuple}")



