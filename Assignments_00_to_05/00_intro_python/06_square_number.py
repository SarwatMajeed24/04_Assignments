    # Asks the user for a number and prints its square.
    
def calculate_square():
    
    try:
        number_str = input("Type a number to see its square: ")
        number = float(number_str)
        square = number * number
        print(f"{number} squared is {square}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    calculate_square()