# 1. Create a list of 5 favorite movies
movies = ["Inception", "Interstellar", "Avengers", "Titanic", "Joker"]

# 2. Create a list with mixed data types
mixed_list = [10, "hello", 3.14, True]

# 3. Create a nested list (list inside another list)
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]

# 4. Access the first element of a list
print(movies[0])

# 5. Access the middle element of a list
print(movies[len(movies)//2])

# 6. Access the last element of a list
print(movies[-1])

# 7. Use negative indexing to get the second-last element
print(movies[-2])

# 8. Print the first 3 elements of a list using slicing
print(movies[:3])

# 9. Print the last 3 elements of a list using slicing
print(movies[-3:])

# 10. Reverse a list using slicing
print(movies[::-1])

# 11. Replace the second element with "Python"
movies[1] = "Python"
print(movies)

# 12. Change the last two elements to "Done" and "Finish"
movies[-2:] = ["Done", "Finish"]
print(movies)

# 13. Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# 14. Repeat a list 3 times
print(list1 * 3)

# 15. Check if "apple" exists in a list
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)

#Working with list methods

numbers = [5, 2, 9, 1, 5, 6]
fruits = ["apple", "banana", "cherry"]

# 1. Append "orange" to fruits
fruits.append("orange")
print(fruits)

# 2. Insert "kiwi" at index 1
fruits.insert(1, "kiwi")
print(fruits)

# 3. Remove "banana"
fruits.remove("banana")
print(fruits)

# 4. Pop the last item from numbers
numbers.pop()
print(numbers)

# 5. Clear all elements from a copy of fruits
fruits_copy = fruits.copy()
fruits_copy.clear()
print(fruits_copy)

# 6. Sort numbers in ascending order
numbers.sort()
print(numbers)

# 7. Sort numbers in descending order
numbers.sort(reverse=True)
print(numbers)

# 8. Reverse fruits without sorting
fruits.reverse()
print(fruits)

# 9. Sort fruits alphabetically
fruits.sort()
print(fruits)

# 10. Count how many times 5 appears in numbers
print(numbers.count(5))

# 11. Find the index of "cherry" in fruits
print(fruits.index("cherry"))

# 12. Create a shallow copy of numbers and modify it
copy_numbers = numbers.copy()
copy_numbers[1] = 100
print("Original:", numbers)
print("Copy:", copy_numbers)
print(id(numbers),id(copy_numbers))


# -------------------------
# 3. Mini Tasks
# -------------------------

# 1. Create a list of 10 numbers and get max
nums = [1, 5, 8, 12, 3, 7, 19, 2, 10, 6]
print(max(nums))

# 2. Get min
print(min(nums))

# 3. Find sum
print(sum(nums))

# 4. Check if all elements are True
print(all([True, True, 1, "yes"]))

# 5. Check if any element is True
print(any([False, 0, "", True]))

# 6. Get length of a list
print(len(nums))

# 7. Convert string "apple" into list of characters
print(list("apple"))

# 8. Create list from tuple
print(list((1, 2, 3, 4)))

# 9. Create list from range 1 to 5
print(list(range(1, 6)))
