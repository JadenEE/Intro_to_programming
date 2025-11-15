def getLoginId(firstName: str, lastName: str, age: int) -> str:
    finalId = firstName[0:2] + firstName[-1] + lastName[-3:] + str(age)
    return finalId

def main():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    age = int(input("Enter age: "))

    loginId = getLoginId(firstName, lastName, age)

    print(f"Your Login ID: {loginId}")

main()