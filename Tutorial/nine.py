#Calculate salary
baseHour = 40
ot = 1.5

hour = float(input("Enter the hour(s) you worked: "))
payRate = float(input("Enter the hourly pay rate: "))

if hour > baseHour:
    overtime = hour - baseHour
    overtimePay = overtime * payRate * ot
    grossPay = baseHour * payRate + overtimePay
else:
    grossPay = hour * payrate

day = hour / 24
month = day / 30
year = day / 365

print(f"The gross pay is RM {grossPay:.2f} in {day:.0f} days or {month:.0f} months or {year:.0f} years. ")
