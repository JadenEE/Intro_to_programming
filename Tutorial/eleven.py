total = 0

for i in range(1, 6):
    bug = int(input(f"Enter the bug for the {i} day: "))
    total = total + bug

print("The total number of bugs collected:", total)
