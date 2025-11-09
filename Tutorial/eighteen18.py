studentsScore = []

def main():
    key = 1
    while key == 1:
        scoreStudent = input("Enter the student's score or press <E> to end: ")
        if scoreStudent == "E" or scoreStudent == "e":
            adjustedTotal = calculatingTotal(studentsScore) - findingLowestScore(studentsScore)
            average = adjustedTotal / (len(studentsScore) - 1)
            print(f"The average score is: {average:,.2f}%")
            key = 0
        else:
            floatifiedScoreStudent = float(scoreStudent)
            studentsScore.append(floatifiedScoreStudent)

def calculatingTotal(scores: list[float]):
    total = 0
    for s in scores:
        total += s

    return total

def findingLowestScore(scores: list[float]):
    lowest = 1000
    for s in scores:
        if lowest > s:
            lowest = s

    return lowest

main()
