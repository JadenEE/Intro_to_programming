import random

def tossCoin():
    value = random.randint(1, 2)

    print("Tossing Coin...")
    
    if value == 1:
        print("Heads")
    else:
        print("Tails")

    print()

for i in range(10):
    tossCoin()
