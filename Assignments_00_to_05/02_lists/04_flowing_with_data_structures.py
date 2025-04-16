from typing import List

def add_three_copies(my_list: List[str], data: str):
    """
    Adds three copies of the given data to the provided list.

    This function demonstrates the mutability of lists in Python. Changes
    made to the list within this function are reflected outside the function
    without needing to return the list.

    Args:
        my_list: The list to which the data will be added (mutable).
        data: The data to be copied and added to the list.
    """
    for _ in range(3):  # Adds the data three times
        my_list.append(data)
    # No return statement is needed because the list is modified in-place.

if __name__ == "__main__":
    message = input("Enter a message to copy: ")
    my_list: List[str] = []  # Initialize an empty list, annotated as a list of strings
    print(f"List before: {my_list}")
    add_three_copies(my_list, message)  # Call the function to modify the list
    print(f"List after: {my_list}")  # Print the list after the function call
