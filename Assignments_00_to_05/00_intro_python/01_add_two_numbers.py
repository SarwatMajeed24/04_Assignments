 #Takes two integer inputs from the user and calculates their sum.
 
def main():
         
    try:
        # Prompt the user to enter the first number
        num1_str = input("Enter the first integer: ")

        # Read the input and convert it to an integer
        num1 = int(num1_str)

        # Prompt the user to enter the second number
        num2_str = input("Enter the second integer: ")

        # Read the input and convert it to an integer
        num2 = int(num2_str)

        # Calculate the sum of the two numbers
        total_sum = num1 + num2

        # Print the total sum with an appropriate message
        print(f"The sum of {num1} and {num2} is: {total_sum}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()