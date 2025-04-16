# def double_until_100():
#     """Asks the user for a number and doubles it until it's 100 or greater."""
#     while True:
#         try:
#             num_str = input("Enter a number: ")
#             number = float(num_str)  # Use float to allow for decimal inputs
#             break  # Exit the loop if input is valid
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

#     while number < 100:
#         print(f"Current value: {number}")
#         number *= 2
#     print(f"Final value: {number}")
#     print("The value has reached or exceeded 100!")

# if __name__ == "__main__":
#     double_until_100()



# def double_until_100():
#     # Ask the user for an initial number
#     number = float(input("Enter a number: "))
    
#     # Keep doubling the number until it is 100 or greater
#     while number < 100:
#         number *= 2
#         print(f"The new value is: {number}")
    
#     print("The value has reached or exceeded 100!")

# # Call the function to start the process
# double_until_100()

def double_until_100():
    """Asks the user for a number and doubles it until it's 100 or greater,
    printing intermediate steps as requested."""
    while True:
        try:
            num_str = input("Enter a number: ")
            start_number = float(num_str)  # Store the initial number
            number = start_number
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Current number is {start_number}")
    while number < 100:
        doubled = number * 2
        print(f"The double of {number} is {doubled}")
        number = doubled
        print(f"The final value: {number}")
    print(f"The final value reached or exceeded 100.")

if __name__ == "__main__":
    double_until_100()