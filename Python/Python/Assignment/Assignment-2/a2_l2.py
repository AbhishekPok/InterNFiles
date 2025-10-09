#Write a program to convert temperature from Celsius to Fahrenheit.
def tempConvert(Cel):
    """Converts the reading of Celsius to Fahrenheit"""
    Fahr = (Cel * (9/5)) + 32
    return round(Fahr, 3)

temp = int(input("Enter the current reading of the Temperature in Celsius:"))
convertedTemp = tempConvert(temp)

print(f"Temperature in Fahrenheit is: {convertedTemp} F")

# Given a circleʼs radius, calculate area and circumference.

def areaOfCircle(Rad):
    """Calculates the area of Circle with given radius"""
    return round((22 / 7) * (Rad ** 2) , 3)
def circumOfCircle(Rad):
    """Calculates the circumference of Circle with given radius"""
    return round(2 * (22 / 7) * Rad, 3)

radius = int(input("Enter the radius of the circle: "))
areaofcircle = areaOfCircle(radius)
circumofcircle = circumOfCircle(radius)

print(f"Area of Circle is: {areaofcircle}")
print(f"Circumference of Circle is: {circumofcircle}")

# Use abs() to find the absolute difference between two numbers.

Diff = circumofcircle - areaofcircle
print(f"Difference between Circumference and Area of Circle is: {Diff}")
theAbsoluteDiff = abs(Diff)
print(f"Absolute Difference between Circumference and Area of Circle is: {theAbsoluteDiff}")

#  Use round() to round 3.14159 to:
# 2 decimal places
# No decimal places

pi = 3.14159
print(f"Given Value of pi is: {pi}")

round2placevalue = round(pi, 2)
roundnoplacevalue = round(pi)

print(f"value of pi after being rounded to 2 decimal places is : {round2placevalue}")
print(f"value of pi after being rounded to nearest integer is : {roundnoplacevalue}")

# Show the effect of floor division with:
# Two positive integers
# Two negative integers
# A positive and a negative integer

positiveNum1 = 2
positiveNum2 = 3
negativeNum1 = -2
negativeNum2 = -3
positiveFloorDiv = positiveNum1 // positiveNum2
negativeFloorDiv = negativeNum1 // negativeNum2
mixedFloorDiv = positiveNum1 // negativeNum2
print(f"Floor Division of two positive numbers {positiveNum1} and {positiveNum2} is: {positiveFloorDiv}")
print(f"Floor Division of two negative numbers {negativeNum1} and {negativeNum2} is: {negativeFloorDiv}")
print(f"Floor Division of mixed numbers {positiveNum1} and {negativeNum2} is: {mixedFloorDiv}")
