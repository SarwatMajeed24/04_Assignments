def double_list_elements_new_list(numbers):
  """
  Returns a new list with each element doubled from the original list.

  Args:
    numbers: A list of numbers (integers or floats).

  Returns:
    A new list where each element is double the corresponding element
    in the input list.
  """
  doubled_numbers = [number * 2 for number in numbers]
  return doubled_numbers

# Example usage of the alternative approach:
original_numbers = [1, 2, 3, 4]
print(f"Original list: {original_numbers}")
new_doubled_list = double_list_elements_new_list(original_numbers)
print(f"New list with doubled elements: {new_doubled_list}")
print(f"Original list (still unchanged): {original_numbers}")