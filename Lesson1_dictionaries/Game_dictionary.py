games = {
    "cricket" : "A bat and ball game.",
    "football" : "A game played by kicking a ball.",
    "chess" : "A board game played using pieces."
}

#menu

print("------- Game Dictionary Menu -------")
print("1. Get Game Description")
print("2. Add a New Game")
print("3. Change Game Description")
print("4. Delete a Game")

choice = input("Enter your choice (1/2/3/4): ")

#Option 1

if choice == "1":
    game=input("Enter Game Name: ").lower()

    if game in games:
        print("Description: ", games[game])
    else:
        print("Game Not Found !!!")

#Option 2

elif choice == "2":
    new_game= input("Enter new game name: ").lower()
    description= input("Enter game description: ")

    games[new_game]= description
    print("Game added successfully !!!")

#Option 3

elif choice == "3":
    game=input("Enter game name to change description: ").lower()

    if game in games:
        new_description=input("Enter new description: ")
        games[game]=new_description
        print("Description updated successfully !!!")
    else:
        print("Game not found !")

#Option 4

elif choice == "4":
    game=input("Enter Game name to be deleted: ").lower()

    if game in games:
        del games[game]
        print("Game deleted successfully !!!")
    else:
        print("Game not found !!!")

else:
    print("Invalid Choice !!!")

print("\n Updated Game Dictionary: ")
print(games)

