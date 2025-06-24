"""
Write a program to get the even numbers from the given number?

Run 1:
Enter any integer: 72146
[2, 4, 6]

Run 2:
Enter any integer: 45580
[4, 8, 0]

Run 3:
Enter any integer: 13579
[]
"""
# method 1
# number=int(input("Enter the number:"))
# snum=str(number)
# lst=[]
# for i in snum:
#     i=int(i)
#     if i%2==0:
#         lst.append(i)
# print(lst)

# method 2 - using math alone
number=int(input("Enter the number:"))
lst = []
while number>9:
    rem = number%10
    if rem%2 == 0:
        lst.insert(0, rem)
    number = number//10
if number%2 == 0:
    lst.insert(0, number)
print(lst)
