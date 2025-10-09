#abbreviation of a word
word = "World Health Organization"
abbreviation = ""
for word in word.split(" "):
    abbreviation += word[0].upper()
print ("\'" + abbreviation + "\'")

#replace one word with another word
text = "Python is a case sensitive language"
print("The original string is : ", text)
#replacing "a case sensitive" with "object oriented"
new_text = text.replace("a case sensitive", "object oriented")
print("The modified string is : ", new_text)    

#creating a ceaser cipher
cipherText = []
for char in text:
    cipherText.append(chr((ord(char) +1)))
cipherText = ''.join(cipherText)
print(f"{cipherText}")
