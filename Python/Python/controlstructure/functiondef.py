#learning about functions in python
#let's start with creating a fibbonaci function
def fibonacci(num):
    a , b = 0, 1
    for i in range(num):
        print (a, end= "")
        a , b = b , a + b
    print (" ")
num = int(input("Enter the number of terms in series you want to print:"))
fibonacci(num)
