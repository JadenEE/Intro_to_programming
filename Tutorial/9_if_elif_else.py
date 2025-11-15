books = int(input("Enter the amount of the book(s) purchased: "))

if books < 2:
    print("You earned 0 point(s).")
elif books >= 2 and books < 4:
    print("You earned 5 point(s).")
elif books >= 4 and books < 6:
    print("You earned 15 point(s).")
elif books >= 6 and books < 8:
    print("You earned 30 point(s).")
else:
    print("You earned 60 point(s).")
