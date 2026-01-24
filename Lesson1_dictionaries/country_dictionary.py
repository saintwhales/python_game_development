countries = {

}

while True:

#options

    print("----- Country Dictionary Menu -----")
    print("1. Insert a new country")
    print("2. Get capital")
    print("3. Change capital")
    print("4. Delete a country")
    print("5. Exit")

    choice = int(input("Select 1, 2,3, 4 or 5: "))

#option 1

    if choice == 1:
        new_country = input("Enter new country name.").lower()
        capital = input("Enter new capital name.").lower()

        countries[new_country] = capital
        print("Country added successfully !")

#option 2

    elif choice == 2:
        country = input("Enter the country name.").lower()

        if country in countries:
            print("Capital: ", countries[country])
        else:
            print("Country not found !")

#option 3

    elif choice == 3:
        country=input("Enter country name to change the capital: ").lower()

        if country in countries:
            new_capital=input("Enter new capital: ")
            countries[country]=new_capital
            print("Capital updated successfully !")
        else:
            print("Country not found !")

#Option 4

    elif choice == 4:
        country=input("Enter country name to be deleted: ").lower()

        if country in countries:
            del countries[country]
            print("Country deleted successfully !")
        else:
            print("Country not found !")

    elif choice == 5:
        print("Goodbye !")
        break

    else:
        print("Invalid Choice !!!")

print("\n Updated country Dictionary: ")
print(countries)