'''
File Management to open file
'''

# f = open('readme.md', "r")
# print(f.name)
# print(f.mode)
# print(type(f))
# f.close()
#
# with open('readme.md', "r") as f:
#     print(f.closed)
#     print(f.name)
# print(f"f.closed: {f.closed}")

'''
File Management to read file
'''

# with open('./readme1.md', "r") as f:
#     content = f.read()
#     print(content)

# with open('readme.md', "w") as f:
#     f.write('Test Print')
#     f.seek()
#     print(f.tell())
#
#     f.write('ab')

with open('readme.md', "r") as f:
    print(f.closed)
    print(f.name)
print(f"f.closed: {f.closed}")
'''
copying content from one file to another
'''
with open('readme.md', "r") as readfile:
    with open('example1.txt', "w") as writefile:
        for line in readfile:
            writefile.write(line)
print("Copying succeed")

pass
