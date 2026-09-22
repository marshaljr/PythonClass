number_input = input("Enter a positive integer with at least 3 digits: ")

try:
    number = int(number_input)

    if number <= 0:
        print("Please enter a positive number.")

    elif len(str(number)) < 3:
        print("Please enter a number with at least 3 digits.")

    else:
        print("\n--- Number Analysis ---")

        print("Decimal:", number)
        print("Binary:", bin(number))
        print("Octal:", oct(number))
        print("Hexadecimal:", hex(number))

        last_digit = number % 10
        print("Last Digit:", last_digit)

        if number % 2 == 0:
            print("Number is: Even")
        else:
            print("Number is: Odd")

except ValueError:
    print("Please enter a valid integer.")