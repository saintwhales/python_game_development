print("----Unique Word Collector Game----")
print("Enter words one by one.")
print("Type 'stop' to finish the game\n")

words = set()

while True:
    word = input("Enter a word: ").lower()
    if word == "stop":
        break
    before_count = len(words)
    words.add(word)
    after_count = len(words)
    if before_count == after_count:
        print("Duplicate word ignored!\n")
    else:
        print("Word added successfully\n")

print("\nGame Over!")
print("Unique Words you entered: ")
for w in words:
    print(w)
print("Total unique words: ", len(words))