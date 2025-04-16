import random
import time  # Import the time module for a slight delay

def roll_dice():
    """Simulates rolling a single die and returns the result."""
    return random.randint(1, 6)

def simulate_dice_rolls_with_details():
    """Simulates rolling two dice and prints the individual rolls before the total."""
    print("Rolling the dice...")
    time.sleep(0.5)  # Add a small delay for visual effect
    die1 = roll_dice()
    die2 = roll_dice()
    print(f"Die 1 rolled: {die1}")
    print(f"Die 2 rolled: {die2}")
    total = die1 + die2
    print(f"Total: {total}")
    return total

def simulate_multiple_rolls(num_rolls):
    """Simulates rolling two dice a specified number of times and prints details for each roll."""
    print(f"Simulating {num_rolls} rolls of two dice:")
    for i in range(num_rolls):
        print(f"\n--- Roll {i + 1} ---")
        simulate_dice_rolls_with_details()

if __name__ == "__main__":
    simulate_multiple_rolls(3)