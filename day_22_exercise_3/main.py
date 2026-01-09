""" Create a program capable of displaying questions to the user like KBC
Use list data type tp store the questions and their correct answers.
Display the final amount the person is taking home after playing the game """

name = input("Enter name: ")
print("Welcome", name)

questions = ["Capital of India?", "National bird of India?"]
answers = ["Delhi", "Peacock"]
money = [1000, 5000]

total = 0

for i in range(2):
    print(questions[i])
    ans = input("Answer: ")

    if ans == answers[i]:
        total = total + money[i]
        print("Correct! You won", money[i])
    else:
        print("Wrong answer")
        break

print("Final amount:", total)
