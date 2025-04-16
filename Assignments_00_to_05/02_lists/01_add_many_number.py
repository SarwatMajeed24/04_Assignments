from typing import Sequence

# Function to calculate the sum of a sequence of numbers (could be int or float)
def sum_of_numbers(numbers: Sequence[float]) -> float:
    # Calculate and return the sum using the built-in sum() function
    return sum(numbers)

# Example usage of the function
if __name__ == "__main__":
    # Sample list of numbers (integers)
    numbers = [10, 20, 30, 40, 50]
    
    # Calling the function and printing the result
    result = sum_of_numbers(numbers)
    print(f"The sum of the numbers is: {result}")
    
    # Example with an empty list
    empty_list: Sequence[float] = [] 
    empty_sum = sum_of_numbers(empty_list)
    print(f"The sum of the empty list {empty_list} is: {empty_sum}")

    # Example with a list of floats
    float_list = [1.5, 2.5, 3.0]
    float_sum = sum_of_numbers(float_list)
    print(f"The sum of the list {float_list} is: {float_sum}")

