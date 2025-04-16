def print_fibonacci_up_to_limit():
    """Prints Fibonacci sequence terms up to a specified maximum value."""
    MAX_VALUE = 10000
    a, b = 0, 1

    print(a, end=" ")
    while b < MAX_VALUE:
        print(b, end=" ")
        a, b = b, a + b
    print()  # Print a newline at the end

if __name__ == "__main__":
    print_fibonacci_up_to_limit()