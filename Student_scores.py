student = {
    "name": "Daniel",
    "marks": {
        "maths": "85/100",
        "english": "75/100",
        "science": "90/100"
    }
}

while True:

#menu

    print("------ Student Scores ------")
    print("1. Insert subject")
    print("2. Get score")
    print("3. Change score")
    print("4. Delete score")
    print("5. Exit \n")

    choice = int(input("Select 1, 2, 3, 4 or 5.\n"))

 #option 1

    if choice == 1:
        new_subject = input("Enter the new subject name.").lower()
        score = input("Enter the new score.").lower()

        student["marks"][new_subject] = score
        print("New subject added succesfully.\n")

#option 2

    elif choice == 2:
        subject = input("Enter the subject name.").lower()
        
        if subject in student["marks"]:
            print(student["marks"][subject])
        else:
            print("Subject not found.\n")

#option 3

    elif choice == 3:
        subject=input("Enter subject name to change the score: ").lower()

        if subject in student["marks"]:
            new_score =input("Enter new score: ")
            student["marks"][subject]=new_score
            print("Score updated successfully.\n")
        else:
            print("Subject not found.\n")

#option 4

    elif choice == 4:
        subject = input("Enter subject name to be deleted: ").lower()

        if subject in student["marks"]:
            del student["marks"][subject]
            print("subject deleted successfully.\n")
        else:
            print("Subject not found.\n")

#option 5

    elif choice == 5:
        print("Goodbye.")
        break
    else:
        print("Invalid Choice.")

print("\n Updated student Dictionary: ")
print(student)