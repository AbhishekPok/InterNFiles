def filehandle():
    # with open('data.txt', "w") as writefile:
    #     writefile.write('''
    #     Python is fun.
    #     File handling makes it powerful.
    #     Exception handling makes it reliable.
    #     ''')
    # print("Writing success.")
    """
       Write a Python program to read the entire contents of data.txt and display it on
       the screen
       """
    # with open('data.txt', "r") as readfile:
    #     result = readfile.read()
    # print(f"The content of the file is :{result}", end = '')
    """
        Write a program to read only the first 10 characters from data.txt .
    """
    # with open('data.txt', "r") as readfile:
    #     result = readfile.read(10)
    # print(f"The content of the file is :\n{result}", end = '')
    """
        Use .readline() to read the first line only
    """
    # with open('data.txt', "r") as readfile:
    #     result = readfile.readline()
    # print(f"The content of the file is :\n{result}", end = '')
    """
        Use a loop with .readline() or .readlines() to display all lines one by one.
    """
    # with open('data.txt', "r") as readfile:
    #     for lines in readfile:
    #         print(lines, end = '')
    """
        Write a program that takes user input and appends it to data.txt without
        overwriting existing content
    """
    # with open("data.txt", "a") as appendfile:
    #     userinput = input("Enter Text to append data.txt:")
    #     appendfile.write(userinput)
    # print("Append completed.")

    """
    Write a program that creates another file named copy.txt and copies all content
    from data.txt into it.
    """
    # with open("data.txt", "r") as readfile:
    #     with open("copy.txt", "w") as writefile:
    #         copytext = readfile.read()
    #         writefile.write(copytext)
    # print("Copying file succeed.")

    """
        Write a program to count the number of words in data.txt .
    """
    # with open("data.txt" , "r") as readfile:
    #     content = readfile.read()
    #     words = content.split( )
    #     print(words)
    #     count = len(words)
    #     print(f"The number of word in the file is: {count}")
    """
        Write a program to find and print the longest word in data.txt .
    """
    # lencount = []
    # with open("data.txt", "r") as readfile:
    #     content = readfile.read()
    #     words = content.split( )
    #     for word in words:
    #         lencount.append(len(word))
    # print(max(lencount))
    """
        Use the tell() and seek() methods to:
            -Print the current file pointer position.
            -Move the file pointer to the beginning and re-read the first line.
    """
    # with open("data.txt", "r") as readfile:
    #     readfile.tell()
    #     print(readfile.read())
    #     readfile.seek(0)
    #     print("Pointer pointing to the start of the file.")
    #     print(readfile.readline())

filehandle()
