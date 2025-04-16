import random

def guess_the_number():
    """Plays a number guessing game with the user."""
    secret_number = random.randint(0, 99)
    attempts = 0

    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess_str = input("Enter a guess: ")
            guess = int(guess_str)
            attempts += 1

            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    guess_the_number()