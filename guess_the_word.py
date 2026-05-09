import random

secret_set = set(
    random.sample(
        [
            "bird",
            "shoe",
            "table",
            "laptop",
            "phone",
            "tree",
            "sky",
            "house",
            "car",
            "plane",
            "field",
            "chair",
            "bed",
            "dog",
            "cat",
        ],
        5,
    )
)
guessed_words = set()
attempts = 0
print("\nWelcome to the guess the secret words game!")
print("I have selected 5 unique words.")
print("Try to guess them all. \n")

while guessed_words != secret_set:
    guess = input("Enter your guess: ")
    attempts += 1
    if not guess.isalpha():
        print("Enter a word!")
        continue
    if guess in guessed_words:
        print("You already guessed that word. ")
    elif guess in secret_set:
        print("Correct Guess!")
        guessed_words.add(guess)
    else:
        print("Wrong guess, Try Again. ")
    print("Your correct guesses so far: ", guessed_words)
    print()

print("Congratulations! You guessed all the words.")
print("The secret words were: ", secret_set)
print("Total Attempts: ", attempts)
