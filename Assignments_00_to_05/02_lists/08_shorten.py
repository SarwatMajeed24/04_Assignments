# Define the MAX_LENGTH as per the requirement
MAX_LENGTH = 3

# Function to shorten the list
def shorten(lst):
    removed_items = []  # List to store removed items

    # While the list is longer than MAX_LENGTH, remove elements from the end
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove and return the last item
        removed_items.append(removed_item)  # Add the removed item to the list

    # Print all removed items in one line
    if removed_items:
        print("Removed items:", " , ".join(removed_items))

# Main function to demonstrate the usage
def main():
    # Initialize an empty list
    lst = []

    # Prompt the user to enter elements one by one
    while True:
        element = input("Enter an element (or press Enter to stop): ")
        if element == "":
            break  # Stop if the user presses Enter without typing anything
        lst.append(element)  # Add the element to the list

    # Call the shorten function with the input list
    shorten(lst)

    # Print the final list after shortening
    print("Final list:", lst)

# Run the program
if __name__ == "__main__":
    main()
