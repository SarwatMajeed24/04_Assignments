def count_number_occurrences(number_list):
    """Counts the occurrences of each number in a list and returns a dictionary."""
    counts = {}
    for number in number_list:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return counts

def main():
    """Prompts the user to enter a list of numbers and prints the count of each number."""
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        numbers_str_list = input_str.split()
        number_list = [int(num) for num in numbers_str_list]

        if not number_list:
            print("The list is empty.")
            return

        occurrences = count_number_occurrences(number_list)

        print("\nNumber Occurrences:")
        for number, count in occurrences.items():
            print(f"The number {number} appears {count} time(s).")

    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")

if __name__ == "__main__":
    main()