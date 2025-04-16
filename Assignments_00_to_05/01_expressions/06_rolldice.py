import random

def roll_die():
    """Simulates rolling a single six-sided die."""
    return random.randint(1, 6)

def simulate_two_dice_roll():
    """Simulates rolling two dice, prints individual results, and their total."""
    print("Rolling the dice...")
    die1 = roll_die()
    die2 = roll_die()
    total = die1 + die2
    print(f"Die 1 rolled: {die1}")
    print(f"Die 2 rolled: {die2}")
    print(f"Total of the two dice: {total}")

if __name__ == "__main__":
    simulate_two_dice_roll()