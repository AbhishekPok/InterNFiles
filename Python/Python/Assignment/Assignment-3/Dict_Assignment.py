# Create a dictionary with keys "name" , "age" , and "city" and print it
exampleDict1 = {"Name":'Abhishek',"age":'22',"city":'Kathmandu'}
print(exampleDict1)

# Access the value of "age" from {"name": "John", "age": 25, "city": "London"} .
exampleDict2 = {"name": "John", "age": 25, "city": "London"}
print(exampleDict2["age"])
# for key,values in exampleDict2.items():
#     print(key)
#     print(values)

# Add a new key-value pair "country": "UK" to an existing dictionary.

exampleDict2["Country"] = "London"
print(exampleDict2)

# Change the value of "city" to "Paris" in a given dictionary.
exampleDict2["city"] = "Paris" 
print(exampleDict2)

# Delete the "age" key from a dictionary.
del exampleDict2["age"]
print(exampleDict2)

# Check if the key "salary" exists in {"name": "Sam", "salary": 5000} .
emplyoeeDetail = {"name": "Sam", "salary": 5000} 
check = "salary" in emplyoeeDetail
if check:
    print("There is Salary in the Dictionary.")

# Merge two dictionaries {1: "a", 2: "b"} and {3: "c", 4: "d"} into one
Dict1 = {1: "a", 2: "b"}
Dict2 = {3: "c", 4: "d"}
Dict1.update(Dict2)
print(Dict1)

# Get all keys and all values separately from a dictionary

key = exampleDict1.keys()
value = exampleDict1.values()
print(f"key:{key},value:{value}")

# Create a dictionary from two lists:
# keys = ["a", "b", "c"] and values = [1, 2, 3]
keys = ["a", "b", "c"] 
values = [1, 2, 3]
combined = dict(zip(keys,values))
print(combined)

# Count how many times each letter appears in "banana" using a dictionary.

freq = {}
word = "banana"
for char in word:
    freq[char] = freq.get(char,0) + 1
print(f"Frequency of each letters appeared: {freq}")

# Write a program to get the key with the maximum value in a dictionary
numbericalDict = {"a":1,"b":20,"v":30,"d":40}
max_key = max(numbericalDict, key = numbericalDict.get)
print(f"The key with max. value is {max_key}")
print(f"The max. value is : {numbericalDict[max_key]}")

# Invert a dictionary so that its values become keys and keys become values.
invDict = dict(zip(numbericalDict.values(),numbericalDict.keys()))
print(invDict)

# Given a nested dictionary of student details, print the names of students who
# scored more than 80 in math.
student_details = {
    "Abhishek": {"age": 22, "grades": {"math": 92, "science": 85, "history": 78}},
    "Bewake": {"age": 22, "grades": {"math": 75, "science": 90, "history": 82}},
    "Saugat": {"age": 22, "grades": {"math": 88, "science": 70, "history": 95}},
    "Avisa": {"age": 22, "grades": {"math": 95, "science": 88, "history": 70}}
}
for student_name, details in student_details.items():
    if "grades" in details and "math" in details["grades"]:
        if details["grades"]["math"] > 80:
            print(student_name)

# Write a program to sort a dictionary by its values in ascending order.
def sortingTheDictionary(input_dict):
    item1 = input_dict.items()
    sortedPairs = sorted(item1, key = lambda item:item[1])
    sorted_Dict = dict(sortedPairs)
    return sorted_Dict

my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}
sorted_by_value_dict = sortingTheDictionary(my_dict)
print(f"Original dictionary: {my_dict}")
print(f"Sorted by value (ascending): {sorted_by_value_dict}")

# Remove all keys from a dictionary that have None as a value.

dictfilteration = {"Name":"Abhishek","Age":"22","Address":None,"Contact":None}
filtered = {}
for key,value in dictfilteration.items():
    if value != None:
        filtered.update({key: value})
print(filtered)