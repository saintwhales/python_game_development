print("---- Password Strenght Checker ----\n")
password = input("Enter your password: ")
unique_chars = set(password)
unique_count = len(unique_chars)
length = len(password)
print("\n Analysing Password....\n")
print("Password length: ", length)
print("Unique characters: ", unique_count)

if unique_count <= 3:
    print("Strength: Very Weak")
elif unique_count <= 6:
    print("Strength: Weak")
elif unique_count <= 10:
    print("Strength: Medium")
else:
    print("Strength: Strong")

    