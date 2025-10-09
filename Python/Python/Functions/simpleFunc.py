'''
Simple example to demostrate the use of function and passing a variable as parameter in the function with no return.
'''

# def message(n):
#     print(f"The message Received. The message is:{n}")

# context = input("Enter the Message here:")
# message(context)

# result  = message(context)
# print(result)
'''
Simple example to demostrate the use of function and passing a variable as parameter in the function with return.
'''

# def add(a, b):
#     '''
#     This Function returns the sum of the provied input
#     parameter a : Type Integerw
#     parameter b : Type Integer
#     then returns the value when called 
#     '''
#     return a + b

# val = int(input("Enter the value of a."))
# val1 = int(input("Enter the value of b."))
# res = add(val, val1)
# print(f"The result is :{res}")
'''
    Local and Global variables
'''

# def func():                              
#     global var    #Incase of variable defined using global, 
#     var = 5       #it sets the var as global variable and the value is set of 5 for whole program.
#     print(f"Inside the Function:{var}")

# var = 6
# func()
# print(f"Outside the Function:{var}")

'''
    Positional Arguments

'''
def add(a, b):
    return a + b

val = int(input("Enter the value of a."))
val1 = int(input("Enter the value of b."))
res = add(val, val1)
print(f"The result is :{res}")
