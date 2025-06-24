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
# method 1
# name=input("enter your name:")
# if len(name)>7:
#     print(f"'{name}' is lengthy")
# else:
#     print(f"'{name}' is short")    

# method 2
name=input("enter your name:")
msg = "lengthy" if len(name)>7 else "short"
print(f"'{name}' is {msg}")