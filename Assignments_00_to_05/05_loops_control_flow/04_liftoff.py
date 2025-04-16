# Approach 1
import time

def spaceship_countdown():
    """Prints the countdown sequence for a spaceship launch."""
    print("Spaceship launch sequence initiated:")
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)  # Pause for 1 second between each number
    print("Liftoff!")

if __name__ == "__main__":
    spaceship_countdown()
    
    
    # Approach 2
# def spaceship_countdown():
#     """Prints the countdown sequence for a spaceship launch."""
#     print("Spaceship launch sequence initiated:")
#     for i in range(10):
#         print(10 - i, end=" ")
#     print("Liftoff!")

# if __name__ == "__main__":
#     spaceship_countdown()