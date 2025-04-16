# Function to print the last element of the list
def get_last_element(lst):
    print(lst[-1])  # Print the last element using negative indexing

# Main code
if __name__ == "__main__":
    # Initialize an empty list
    user_list = []

    # Get the number of elements in the list from the user
    n = int(input("How many elements do you want to enter? "))

    # Prompt the user to enter each element of the list
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)  # Add the element to the list

    # Call the function to get and print the last element of the list
    get_last_element(user_list)
