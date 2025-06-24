"""
Write program to get any string and check if its a palindrome?

Run 1:
Enter any string: Ragu
No, Ragu != ugaR

Run 2:
Enter any string: madam
Yes, madam == madam

Run 3:
Enter any string: Lal
No, Lal != laL
"""
# method 1
# a=input("enter any string:")
# lst=list(a)
# lst.reverse()
# b="".join(lst)
# if a==b:
#     print(f"Yes, {a} == {b}")
# else:
#     print(f"No, {a} != {b}")

# method 2
# a = input("Enter any string:")
# b = []
# for i in a:
#     b.insert(0, i)
# b = "".join(b)
# if a == b:
#     print(f"Yes, {a} == {b}")
# else:
#     print(f"No, {a} != {b}")

# method 3
# a = input("Enter any string:")
# b = ''
# lst = list(a)
# while lst:
#     last = lst.pop()
#     b += last
# if a == b:
#     print(f"Yes, {a} == {b}")
# else:
#     print(f"No, {a} != {b}")

# method 4
a = input("Enter any string:")
b = a[::-1]
if a == b:
    print(f"Yes, {a} == {b}")
else:
    print(f"No, {a} != {b}")
