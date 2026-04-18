print("----Quiz Answer Checker----")
print("-"*40)
print("Enter the question numbers you got correct (separated by space):")
print("Example: 1 3 4 7\n")

correct_answers = {1,2,4,6,7}
user_input = input("Enter your answers: ")
student_answers = set(map(int, user_input.split()))
print("\nChecking Results....\n")
right = student_answers.intersection(correct_answers)
wrong = student_answers.difference(correct_answers)
missed = correct_answers.difference(student_answers)

print("Correctly Answerd Questions: ", right)
print("Wrong Answers: ", wrong)
print("Missed Answers ", missed)

score = len(right)
total = len(correct_answers)

print("\nFinal Score: ", score, "/", total)