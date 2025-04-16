# Approach 1

def is_leap_year(year):
    """Checks if a given year is a leap year according to the Gregorian calendar rules."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    """Reads a year from the user and tells whether it's a leap year or not."""
    try:
        year_str = input("Enter a year: ")
        year = int(year_str)

        if is_leap_year(year):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")

    except ValueError:
        print("Invalid input. Please enter a valid whole number for the year.")

if __name__ == "__main__":
    main()
    
 #Approach 2
 
# def main():
#     # Ask the user to input a year
#     year = int(input("Enter a year: "))

#     # Check if the year is a leap year based on the given criteria
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("That's a leap year!")
#     else:
#         print("That's not a leap year.")

# # Call the main function
# if __name__ == "__main__":
#     main()
