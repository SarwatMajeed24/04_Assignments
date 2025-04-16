def main():
    # The affirmation that the user must type correctly
    affirmation = "I am capable of doing anything I put my mind to."
    
    while True:
        # Prompt the user to type the affirmation
        user_input = input("Please type the following affirmation: " + affirmation + "\n")
        
        # Check if the input matches the affirmation
        if user_input == affirmation:
            print("That's right! :)")
            break  # Exit the loop if the user typed the affirmation correctly
        else:
            print("Hmmm That was not the affirmation.")  # Let the user know they were incorrect

# Call the main function to start the program
if __name__ == "__main__":
    main()
