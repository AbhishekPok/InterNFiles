# "The weakest link in cybersecurity is the human being" — Kevin Mitnick
# 1. Length & Indexing
#       -Store your favorite quote in a variable.
#       -Print its length.
#       -Print the first and last characters
quote = "The weakest link in cybersecurity is the human being"
print(len(quote))
print(quote[0], quote[-1])

#2. Concatenation
#   -Store your first name and last name in separate variables.
#   -Combine them into one string with a space in between.
first_name = "Abhishek"
last_name = "Pokhrel"
#concatenating using operator
full_name = first_name + " " + last_name
print(full_name)
#concatenating using f-string
full_name1 = f"{first_name} {last_name}"
print(full_name1)

#3. Repetition
#   Print "Python!" 10 times in a single line.
word = "Python!"
print(word*10)


