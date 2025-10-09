#slicing
word = "I love Python"
print(word[2:6])  # Output: love
print(word[-7:])  # Output: y
#word[0:3] means starting from index 0 to index 2 (3-1)
#incase of negative indexing, -1 is the last index, -2 is the second last index and so on.
print(word[::-1])  # Output: nohtyP evol I
#explanation of word[::-1] is starting from the last index to the first index with a step of -1 ie going backwards
#jumping
print(word[0::2])  # Output: Ioe yhn
#the print(word[0::2]) means starting from index 0 to the end of the string, jump 2 steps each time.ie 0,2,4,6,8,10,12
