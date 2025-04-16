
# Program to continuously add user input to a list and print it when Enter is pressed without typing anything

def main():
    # Initialize an empty list to store the values
    user_list = []
    
    while True:
        # Ask the user to enter a value
        value = input("Enter a value: ")
        
        # If the input is empty (user pressed Enter without typing), break the loop
        if value == "":
            print("Here's the list:", user_list)
            break
        
        # Add the entered value to the list
        user_list.append(value)

# Run the main function
if __name__ == "__main__":
    main()
