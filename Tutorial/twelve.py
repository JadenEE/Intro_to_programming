#My answer for the question

cal_per_min = 4.2
after_five = cal_per_min * 5
total = 0

for i in range(10, 31, 5):
    total = cal_per_min * i
    print(f"The total calories burn in {i} minutes:", total)

#Ignore this part
print(f"{'-' * 80}")

#Miss's answer for the question

cal_per_min = 4.2

for minute in [10, 15, 20, 25, 30]:
    print(f"The total calories burn in {minute} minutes:", cal_per_min * minute)
