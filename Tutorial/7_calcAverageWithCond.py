#Calculate the score
highscore = 95

test1 = int(input("Enter test 1 score: "))
test2 = int(input("Enter test 2 score: "))
test3 = int(input("Enter test 3 score: "))

average = (test1 + test2 + test3) / 3

print(f"The average score is {average}.")

if average >= highscore:
    print("Congratulations!")
    print("You have done a great job!")
