foods = [
    "Scone",
    "Macaroon",
    "Canai Bread",
    "Lemak Rice",
    "Honey Lemon",
    "Pulled Tea"
]

orderCart = []

loopKey = 1

while loopKey == 1:
    print("<*>----------------------------<*>")
    print("    Welcome To ItP Restaurant!")
    print("<*>----------------------------<*>")
    print()
    print("----------MENU----------")
    print(f"Name{'Price':>20}")
    print()
    print("Scone  ----------  RM8.37")
    print("Macaroon  ----------  RM15.15")
    print("Canai Bread  ----------  RM5.00")
    print("Lemak Rice  ----------  RM12.34")
    print("Honey Lemon  ----------  RM3.00")
    print("Pulled Tea  ----------  RM4.10")
    print()

    print("Enter your order by typing the food name || Type [done] to pay")
    userInput = input(">> ")

    if userInput == "done" or userInput == "Done" or userInput == "DONE":
        print("\n==========RESTAURANT'S RECEIPT==========")
        print(f"Name{'Quantity':>20}{'Price Per Unit':>25}\n")
        price = 0
        pricePerUnit = 0
        subTotal = 0

        for order in orderCart:
            if order[0] == "Scone":
                pricePerUnit = 8.37
                price = pricePerUnit * order[1]
            elif order[0] == "Macaroon":
                pricePerUnit = 15.15
                price = pricePerUnit * order[1]
            elif order[0] == "Canai Bread":
                pricePerUnit = 5.00
                price = pricePerUnit * order[1]
            elif order[0] == "Lemak Rice":
                pricePerUnit = 12.34
                price = pricePerUnit * order[1]
            elif order[0] == "Honey Lemon":
                pricePerUnit = 3.00
                price = pricePerUnit * order[1]
            elif order[0] == "Pulled Tea":
                pricePerUnit = 4.10
                price = pricePerUnit * order[1]
            else:
                pricePerUnit = -1
                price = 0
            subTotal += price
            print(f"{order[0]}  ----------  {order[1]}  ----------  RM{pricePerUnit}")

        serviceCharge = subTotal * 0.1

        print("========================================")
        print(f"Subtotal  ----------  RM{subTotal:.2f}")
        print(f"Service Charge (10%)  --  RM{serviceCharge:.2f}")
        print(f"Grand Total ----------  RM{subTotal + serviceCharge:.2f}")
        print("========================================")
        print()
        print("Thanks for dining! Have a wonderful day!")
        input("Press <Enter> to continue...")

        loopKey = 0
    elif userInput in foods:
        print("Input the amount of the food")
        amount = int(input(">> "))

        if amount > 0:
            newOrder = [userInput, amount]
            orderCart.append(newOrder)
        else:
            print("Your amount must be greater than 0!")
    else:
        print("Invalid input, please try again.")