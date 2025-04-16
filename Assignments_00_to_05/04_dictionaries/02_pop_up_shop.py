def main():
    """
    Main function to define fruit prices and calculate the total cost.
    """
    fruit_prices = {
        "apple": 1.50,
        "banana": 1.20,
        "orange": 1.05,
        "mango": 1.75,
        "grape": 2.00,
        "strawberry": 3.00
    }

    final_cost = calculate_total_cost(fruit_prices)

    print(f"\nYour total cost for the selected fruits is: ${final_cost:.2f}")
    print("Thank you for shopping at our fruit shop!")

def calculate_total_cost(fruit_prices):
    """
    Calculates the total cost of fruits the user wants to buy.

    Args:
        fruit_prices (dict): A dictionary where keys are fruit names (str)
                             and values are the price per fruit (float).

    Returns:
        float: The total cost of all the fruits the user wants to buy.
    """
    total_cost = 0.0
    print("Available fruits and prices:")
    for fruit, price in fruit_prices.items():
        print(f"- {fruit}: ${price:.2f} each")

    print("\nLet's calculate your order:")
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity_str = input(f"How many {fruit} would you like to buy? (Enter 0 if none): ")
                quantity = int(quantity_str)
                if quantity >= 0:
                    break
                else:
                    print("Please enter a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        total_cost += quantity * price

    return total_cost

if __name__ == "__main__":
    main()