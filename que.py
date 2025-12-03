# First Question

POUND_TO_KILO = 0.454

userInput = float(input("Enter the object in pounds: "))
converted_value = userInput * 0.454

print("The object in kilograms is", "{:,.2f}".format(converted_value), "kg")

# Second Question

writefile = open("things.txt", "w")

writefile.write("Animal: Spongiforma squarepantsii\n")
writefile.write("Fruit: Buddha's Hand\n")
writefile.write("Country: Bosnia and Herzegovina\n")

writefile.close()

# Third Question

UNDERWEIGHT = 18.5
OVERWEIGHT = 25

weight = float(input("Enter your weight (Pounds): "))
height = float(input("Enter your height (Inches): "))

bmi = (weight * 703) / (height ** 2)

if bmi >= UNDERWEIGHT or bmi <= OVERWEIGHT:
    print("Your weight is optimal. You are normal.")
elif bmi < UNDERWEIGHT:
    print("You are underweight! You are abnormal.")
elif bmi > OVERWEIGHT:
    print("You are overweight! You are obesity.")
