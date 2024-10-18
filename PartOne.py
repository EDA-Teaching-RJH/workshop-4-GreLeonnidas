x = input("What is your First name")
for my_char in x:
    print(my_char, end="")
    if my_char.islower():
        print(my_char)
    if my_char.isupper():
        print("_",my_char.lower(),end="")
print()