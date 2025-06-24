"""
Write a program to check if the given name is lengthy?
Hint: if length is more than 7 then its lengthy

Run 1:
Enter your name: Ram
'Ram' is short

Run 2:
Enter your name: Sathyanarayanan
'Sathyanarayanan' is lengthy
"""
name=input("enter your name:")
if len(name)>7:
    print(f"'{name}' is lenghty")
else:
    print(f"'{name}' is short")    