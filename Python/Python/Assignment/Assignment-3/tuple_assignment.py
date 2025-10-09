#Basic and Syntax checking
# 1. Create a tuple containing five colors. Print the second and fourth color.
colors_Tuple = ("Red","Green","Blue","Purple","Pink")
print(f"The tuple is created : {colors_Tuple} and the type is : {type(colors_Tuple)}")
print(f"The 2nd and 4th color entered is:{colors_Tuple[1]} and {colors_Tuple[3]}")

# 2. Create a tuple with a single element. Verify its type is tuple .
single_tuple = ("Abhishek is Great.")
print(f"The tuple with single elements is created : {single_tuple} and it's type is :{type(single_tuple)}")

# Convert the list ["apple", "banana", "cherry"] into a tuple.
fruitsList = ["apple", "banana", "cherry"]
fruitsTuple = tuple(fruitsList)
print(f"The initial list is : {fruitsList} while after it's converted it is:{fruitsTuple}{type(fruitsTuple)}")

# Concatenate two tuples (1, 2, 3) and (4, 5, 6) into one tuple.
temptuple1 = (1, 2, 3)
temptuple2 = (4, 5, 6)
concateTuple = temptuple1 + temptuple2
print(f"The inital tuples were \n{temptuple1} \n{temptuple2} \nConcateted tuples = {concateTuple}")

# Check whether "python" exists in the tuple ("java", "python", "c++") .
language = ("java", "python", "c++")
print(f"\"python\" is in the Tuple: {"python" in language}")

# Medium Uses:
# Given nums = (10, 20, 30, 40) , unpack them into four variables and print each.
nums = (10, 20, 30, 40)
var1 , var2 , var3 , var4 = nums
print(f"The elements in the Tuple are:{nums}")
print(f"Elements unpacked, stored and printed as : {var1},{var2},{var3},{var4}")

# Find the index of the first occurrence of 5 in (1, 5, 7, 5, 9) .
occurence = (1, 5, 7, 5, 9)
for _ in occurence:
    if _ == 5:
        print(f"The index of the first appearence of \"5\" is : {occurence.index(_)}")
        break

# Given t = ("a", "b", "c", "d", "e") , slice the tuple to get ("b", "c", "d") .
tupleT = ("a", "b", "c", "d", "e")
sliced = tupleT[1:4]
print(f"The sliced tuple is : {sliced} from {tupleT}")

# Count how many times 2 appears in (2, 4, 2, 6, 2, 8) .

countTuple = (2, 4, 2, 6, 2, 8)
print(f"The number of times the element \"2\" appeared in the Tuple is : {countTuple.count(2)}")

# Merge two tuples and sort them into a new tuple.

mergedTuple = occurence + countTuple # occurence taken from line 33 and countTuple from line 47.
sortedMergedTuple = sorted(mergedTuple)
print(f"The Tuple considered are : \n{occurence}\n{countTuple}\nMerged new tuple:{mergedTuple}\nFinally sorted new tuple:{sortedMergedTuple}")

# Write a program to remove an element from a tuple (without directly modifying it).
exampleTuple1 = (10,20,30,40,50)
print(f"Initial Tuple is: {exampleTuple1}")
listConversion = list(exampleTuple1) #Since Tuple is immutable changing it to list.
listConversion.remove(40)
exampleTuple1 = tuple(listConversion)
print(f"After Removal of the any elements say \"40\" in the Initial Tuple: {exampleTuple1}.")

# Given t = (("a", 1), ("b", 2), ("c", 3)) , convert it into a dictionary.
givenTuplet = (("a", 1), ("b", 2), ("c", 3))
changed = dict(givenTuplet)
print(f"Before the conversion: {givenTuplet}\nAfter the conversion: {changed}")

# Swap two tuples:
# t1 = (1, 2) and t2 = (3, 4) → after swap t1 = (3, 4) , t2 = (1, 2) .
t1 = (1, 2)
t2 = (3, 4)
print(f"Before swapping : t1 = {t1}, t2 = {t2}")
b = (t1[0],t1[1])
t1= (t2[0],t2[1])
t2 = b
print(f"After Swapping : t1 = {t1}, t2 = {t2}")

# Reverse a tuple without using slicing.
tupleT #tupleT taken from line 41
listTupleT = list(tupleT)
listTupleT.reverse()
reverseTuple = tuple(listTupleT)
print(f"Initial state :{tupleT} after the reversion: {reverseTuple}")

# 5. Create a tuple from user input where values are comma-separated.
inputFromClient = input("Enter the Elements for tuple seperated by comma (,).")
newlist = inputFromClient.split(',')
inputTuple = tuple(newlist)
print(f"The input is stored in the tuple as follow: {inputTuple}")


