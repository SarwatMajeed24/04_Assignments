import math

def calculate_hypotenuse():
    """
    Asks the user for the lengths of the two perpendicular sides of a
    right triangle and outputs the length of the hypotenuse using the
    Pythagorean theorem.
    """
    try:
        ab_str = input("Enter the length of AB: ")
        ab = float(ab_str)

        ac_str = input("Enter the length of AC: ")
        ac = float(ac_str)

        if ab < 0 or ac < 0:
            print("Side lengths cannot be negative. Please enter non-negative values.")
            return

        # Apply the Pythagorean theorem: BC^2 = AB^2 + AC^2
        bc_squared = ab**2 + ac**2
        bc = math.sqrt(bc_squared)

        print(f"The length of BC (the hypotenuse) is: {bc}")

    except ValueError:
        print("Invalid input. Please enter valid numbers for the side lengths.")

if __name__ == "__main__":
    calculate_hypotenuse()