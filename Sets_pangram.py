def is_pangram(text):
    text = text.lower()
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    text_set = set(text)
    if alphabets.issubset(text_set):
        return "It is a pangram."
    else:
        return "it is not a pangram."
    
sentence = input("Enter a sentence: ")
print(is_pangram(sentence))