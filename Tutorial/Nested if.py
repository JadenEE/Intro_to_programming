#Calculate test score

A = 90
B = 80
C = 70
D = 60

score = int(input("Enter your score: "))

if score >= A:
    print("Congratulations! Your grade is A")
else:
    if score >= B:
        print("Well Done! Your grade is B")
    else:
        if score >= C:
            print("Keep Progressing! Your grade is C")
        else:
            if score >= D:
                print("Read more books bro! Your grade is D")
            else:
                print("Your grade is F. You should consider on taking other course.")
