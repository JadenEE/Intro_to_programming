amount1 = float(input("Enter Amount 1: "))
amount2 = float(input("Enter Amount 2: "))

if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print("The greater value is", amount1)
        else:
            print("The greater value is", amount2)
