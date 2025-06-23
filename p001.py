"""
Write a program to get a number print if its divisible by 5?
Don't use % 

Run 1:
Enter any integer: 40
Yes, 40 is divisible by 5

Run 2:
Enter any integer: 75
Yes, 75 is divisible by 5

Run 3:
Enter any integer: 41
No, 41 is divisible by 5
"""
# method 1
# n=int(input("enter the number:"))
# if n%5==0:
#     print(f"Yes,{n} is divisible by 5")
# else:
#      print(f"no,{n} is  not divisible by 5")    

# method 2
# a=input('enter the number:')
# if a[-1]=='0':
#     print(f"Yes,{a} is divisible by 5")
# elif a[-1]=='5':
#     print(f"Yes,{a} is divisible by 5")    
# else:
#     print(f"no,{a} is  not divisible by 5")

# method 3
n=int(input("enter the number:"))
status=False#assuming the number to be non divisible by 5
a=n
while a>=5:
    a=a-5
    if a==0:
        status=True#our assumption is wrong
        break
if status==True:
    print(f"Yes,{n} is divisible by 5")
else:
    print(f"no,{n} is  not divisible by 5")