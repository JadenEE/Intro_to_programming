# Question 1

def main():
    firstName = str(input("Enter First Name: "))
    lastName = str(input("Enter Last Name: "))

    fullName = f"{firstNameTitleCase(firstName)} {lastNameUpperCase(lastName)}"

    print()
    print(f"Your initials: {initialsName(firstName, lastName)}")
    print(f"Your full name: {fullName}")
    print(f"Your Username: {usernameFormat(firstName, lastName)}")

def firstNameTitleCase(name: str) -> str:
    finalName = name.title()
    return finalName

def lastNameUpperCase(name: str) -> str:
    finalName = name.upper()
    return finalName

def usernameFormat(firstName: str, lastName: str) -> str:
    finalUsername = ""

    for name in firstName:
        finalUsername += name
        break

    finalUsername += lastName
    return finalUsername

def initialsName(firstName: str, lastName: str) -> str:
    firstInitials = ""
    lastInitials = ""

    for i in firstName:
        firstInitials += i
        break

    for i in lastName:
        lastInitials += i
        break

    fullInitials = f"{firstInitials}.{lastInitials}."
    return fullInitials

main()

# Question 2

def main2():
    number = int(input("Enter an INTEGER Number: "))

    print()
    print(f"The sum of all the single-digit numbers is: {numberSummer(str(number))}")

def numberSummer(number: str) -> int:
    total = 0
    for i in number:
        total += int(i)

    return total

main2()
