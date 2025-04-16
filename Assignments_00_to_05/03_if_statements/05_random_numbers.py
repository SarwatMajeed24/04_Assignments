import random

def generate_random_numbers():
    """Prints 10 random numbers in the range of 1 to 100."""
    for _ in range(10):
        random_number = random.randint(1, 100)
        print(random_number, end=" ")  # Print each number followed by a space
    print()  # Print a newline at the end

if __name__ == "__main__":
    generate_random_numbers()
