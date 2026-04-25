import random
secret_set = set(random.sample(range(1,21), 5))
guessed_numbers = set()
attempts = 0
print("\nWelcome to the guess the secret set game!")
print("I have selected 5 unique numbers between 1 and 20.")
print("Try to guess them. \n")

while guessed_numbers != secret_set:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess in guessed_numbers:
        print("You already guessed the number. ")
    elif guess in secret_set:
        print("Correct Guess!")
        guessed_numbers.add(guess)
    else:
        print("Wrong guess, Try Again. ")
    print("Your correct guesses so far: ", guessed_numbers)
    print()

print("Congratulations! You guessed all the numbers.")
print("Secret set was: ", secret_set)
print("Total Attempts: ", attempts)