import random
secret_set = set(random.sample(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], 5))
guessed_letters = set()
attempts = 0
print("\nWelcome to the guess the secret letters game!")
print("I have selected 5 unique letters.")
print("Try to guess them. \n")

while guessed_letters != secret_set:
    guess = input("Enter your guess: ")
    attempts += 1
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only ONE letter!")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter. ")
    elif guess in secret_set:
        print("Correct Guess!")
        guessed_letters.add(guess)
    else:
        print("Wrong guess, Try Again. ")
    print("Your correct guesses so far: ", guessed_letters)
    print()

print("Congratulations! You guessed all the letters.")
print("The secret letters were: ", secret_set)
print("Total Attempts: ", attempts)