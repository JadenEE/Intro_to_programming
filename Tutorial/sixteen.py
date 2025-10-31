# This program counts the number of times
# the letter T (uppercase or lowercase)
# appears in a string.

def main():
    # Create a variable to use to hold the count
    # The variable must start with 0
    count = 0

    # Get a string from the user.
    my_string = input("Enter a sentence: ")

    # Count the Ts.
    for ch in my_string:
        if ch == "S" or ch == "s":
            count += 1

    # Print the result
    print(f"The letter S appears {count} times.")


if __name__ in '__main__':
    main()
