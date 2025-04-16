def main():
    """Prints the first 20 even numbers."""

    # Approach 1: Iterating and checking for even numbers
    print("First 20 even numbers (Approach 1):")
    count = 0
    number = 0
    while count < 20:
        if number % 2 == 0:
            print(number)
            count += 1
        number += 1

    print("\nFirst 20 even numbers (Approach 2):")
    # Approach 2: Directly generating even numbers
    for i in range(20):
        even_number = 2 * i
        print(even_number)

    print("\nFirst 20 even numbers (Approach 3):")
    # Approach 3: Iterating with a step of 2
    for i in range(0, 40, 2):
        print(i)

if __name__ == "__main__":
    main()