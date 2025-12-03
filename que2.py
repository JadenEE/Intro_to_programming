# Third Question

UNDERWEIGHT = 18.5
OVERWEIGHT = 25

weight = float(input("Enter your weight (Pounds): "))
height = float(input("Enter your height (Inches): "))

bmi = (weight * 703) / (height ** 2)

if bmi >= UNDERWEIGHT and bmi <= OVERWEIGHT:
    print("Your weight is optimal. You are normal.")
elif bmi < UNDERWEIGHT:
    print("You are underweight! You are abnormal.")
elif bmi > OVERWEIGHT:
    print("You are overweight! You are obesity.")

print(f"Your BMI: {bmi:,.2f}")
