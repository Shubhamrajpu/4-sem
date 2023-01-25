user1=int(input("enter the first number"))
user2=int(input("enter the second number"))
user3=int(input("enter the third number"))
temp1 = 0
temp2 = 0
temp3 = 0
if (user1 % 2!=0) and (user1>user2 and user1>user3):
    print(user1, " is max")

elif (user2 %2!=0) and (user2 > user1 and user2 > user3):
     print(user2, " is max")

elif (user3 %2!=0) and (user3 > user1 and user3 > user2):
    print(user3, " is max")
else:
    print("no odd number")
