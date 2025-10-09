#split
file="example.txt"
name =(file.split("."))[0]
extension=(file.split("."))[1]
print(f"name of the file: {name}")      # Output: example
print(f"extension of the file: {extension}") # Output: txt
