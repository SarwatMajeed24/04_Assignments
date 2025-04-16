# def feet_to_inches():
#     """Converts a measurement in feet to inches."""
#     while True:
#         feet_input = input("Enter the measurement in feet (or 'quit' to exit): ")
#         if feet_input.lower() == 'quit':
#             break
#         try:
#             feet = float(feet_input)
#             if feet >= 0:
#                 inches = feet * 12
#                 print(f"{feet} foot is equal to {inches} inches.")
#             else:
#                 print("Measurement in feet cannot be negative. Please enter a non-negative value.")
#         except ValueError:
#             print("Invalid input. Please enter a valid number for feet or 'quit'.")

# if __name__ == "__main__":
#     feet_to_inches()

"""
An example program with constants
"""

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")
    
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()