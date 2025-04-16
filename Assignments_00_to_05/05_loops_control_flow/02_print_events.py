def print_first_20_even_numbers():
    """Prints the first 20 even numbers using a loop."""
    count = 0
    number = 0
    while count < 20:
        if number % 2 == 0:
            print(number)
            count += 1
        number += 1

if __name__ == "__main__":
    print_first_20_even_numbers()