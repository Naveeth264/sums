"""
Write a program to get an integer and print its singular digit?
Example:
12 -> 1+2 -> 3
29 -> 2+9 -> 11 -> 1+1 -> 2
78 -> 7+8 -> 15 -> 1+5 -> 6
108 -> 1+0+8 -> 9

Run 1: 
Enter any integer: 77
5

Run 2: 
Enter any integer: 89
8
"""
# method 1
# num = int(input("Enter any intger:"))
# while num > 9:
#     snum = str(num)
#     lst = [int(i) for i in snum ]
#     print(lst)
#     num = sum(lst)
# print(num)
#  method 2
num =int(input("Enter any intger:"))
while num>9:
    tot=0
    a=str(num)
    for i in a:
        tot+=int(i)
    num=tot
print(num)       