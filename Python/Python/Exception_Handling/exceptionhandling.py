def exceptionhandling ():
    """
        Write a program that asks the user to enter a number and divides 100 by that
        number.
        Handle ZeroDivisionError and display an appropriate message.
    """
    # take = int(input("Enter any number:"))
    # try :
    #     operation = 100 / take
    # except ZeroDivisionError:
    #     print("Please do not enter the value zero. \nExiting from the Script")

    """
        Write a program that tries to open a file named missing.txt .
        Handle FileNotFoundError gracefully.
    """
    # try:
    #     with open("missing.txt", "r") as readfile:
    #         context = readfile.read()
    #         print(f"The content in the file:{context}")
    # except FileNotFoundError:
    #     print("File not present in the working Directory. \nPlease verify and try again.")

    """
         Write a program to take a number from the user and convert it into an integer.
        Handle ValueError if the user enters invalid input.
    """
    # try:
    #     take = int(input("Enter any value:"))
    # except ValueError:
    #     print("Please enter any integer value,\nanything other than that is not acceptable.")
    """
       Combine file handling with exception handling:
            Ask the user to enter a filename.
            Try to open and read the file.
            If the file doesnʼt exist, print a message like 
    """
    # filename = input("Enter the name of the file you want to open:")
    # try:
    #     with open(f"{filename}.txt", "r") as readfile:
    #         content = readfile.read()
    # except FileNotFoundError:
    #     print("The file you've searched doesn't exist in the current working directory.\nPlease try again, exiting the code.")
    """
        Create a program that writes a list of numbers into a file. Then read back the file and calculate the sum of numbers.
        Add exception handling for ValueError (in case non-numeric data is inside the file).
    """
    # numlist = [1,2,3,4,5,6,7,8,9,10,]
    # contentlist = []
    # with open("sumfile.txt", "w") as writefile:
    #     for num in numlist:
    #         writefile.writelines(f"{str(num)}\n")
    # try:
    #     with open("sumfile.txt", "r") as readfile:
    #         content = readfile.read()
    #         textlist = content.split()
    #         # print(textlist)
    #         for value in textlist:
    #                 cast = int(value)
    #                 contentlist.append(cast)
    #         print(f"{sum(contentlist)}")
    # except ValueError:
    #     print("Invalid Structure seen in the file.")
    """
        Write a program with a finally block that always closes the file after reading,
        even if an exception occurs.
    """
    readfile = open("sumfile.txt", "r")
    try:
        pass
    except:
        pass





exceptionhandling()