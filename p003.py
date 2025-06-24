"""
Write a program to get name of the user and print lucky if the name starts with vowel?

Run 1:
Enter your name: Abi
Lucky

Run 2:
Enter your name: abi
Lucky

Run 3:
Enter your name: Ram
Unlucky
"""
# methos 1
# a=input("Enter your name:")
# s=['a','e','i','o','u']
# fc=a[0].lower()
# if fc in s:
#     print("Lucky")
# else:
#     print("Unlucky")    

# method 2
a = input("Enter your name:")
vowels = "aeiouAEIOU"
if a[0] in vowels:
    print("Lucky")
else:
    print("Unlucky")