def perform_division_with_remainder():
    """
    Asks the user for two integers, performs division, and prints
    the quotient and the remainder.
    """
    try:
        numerator_str = input("Please enter an integer to be divided: ")
        numerator = int(numerator_str)

        denominator_str = input("Please enter an integer to divide by: ")
        denominator = int(denominator_str)

        if denominator == 0:
            print("Error: Cannot divide by zero.")
            return

        quotient = numerator // denominator  # Integer division
        remainder = numerator % denominator  # Modulo operator for remainder

        print(f"The result of this division is {quotient} with a remainder of {remainder}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    perform_division_with_remainder()