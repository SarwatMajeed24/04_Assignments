def check_height():
    """Asks the user for their height and checks if they meet the minimum height requirement."""

    minimum_height = 50  # Assuming the height unit is consistent

    try:
        height_str = input("How tall are you? (Please enter a numerical value): ")
        user_height = float(height_str)  # Allow for decimal heights

        if user_height > minimum_height:
            print(f"You are taller than the minimum height of {minimum_height}.")
            print("Enjoy the ride!")
        elif user_height == minimum_height:
            print(f"You are exactly the minimum height of {minimum_height}.")
            print("You can ride, but please be aware of the safety guidelines.")
        else:
            print(f"Sorry, you are shorter than the minimum height of {minimum_height}.")
            print("You are not tall enough for this ride.")

    except ValueError:
        print("Invalid input. Please enter a numerical value for your height.")

if __name__ == "__main__":
    check_height()