# word = ["cat", "window", "defenestrate"]
# for w in word:
    # length = len(w)
    # print(f"{w}, {length}")
user = {'abhishek': 'active','saugat': 'inactive', 'abhisha':'active'}
#strategy:  Iterate over a copy of the collection
for name,status in user.copy().items():
    print(f"{name}, {status}")
    if status == 'inactive':
        del user[name]
print("list of active users:")
print(user)

# Strategy:  Create a new collection
active_users = {}
for user, status in user.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

#for loop containing break, continue and else statements

#for loop containing break and else statements
for n in range(2, 10): #outer loop to iterate from 2 to 9
    for x in range(2,n):#inner loop to iterate from 2 to n-1
        if n % x == 0: #check if n is divisible by x
            print(f"Found a composite number {n}") #if composite print it
            break #exit the loop
    else: #if no break occurs
        print(f"Found a prime number {n}")

#for loop containing continue statement
for num in range(2, 10): #iterate from 2 to 9
    if num % 2 == 0: #check if num is even
        print(f"Found an even number {num}") #if even print it
        continue #skip the rest of the loop
    print(f"Found an oddnumber {num}") #if odd print it