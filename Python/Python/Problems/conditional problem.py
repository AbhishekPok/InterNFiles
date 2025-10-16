"""
1. Age Group Categorization
Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
"""
# ageinput = int(input("Enter your age here:"))
#
# if ageinput < 13 :
#     print("You are Included inside \"CHID\"")
# elif ageinput < 20 :
#     print("You are Included inside \"TEENAGER\"")
# elif ageinput < 60 :
#     print("You are Included inside \"ADULT\"")
# else:
#     print("You are Included inside \"SENIOR\"")
"""
Movie Ticket Pricing
Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
"""
age = 22
day = "Wednesday"

price = 12 if age >=18 else 8
