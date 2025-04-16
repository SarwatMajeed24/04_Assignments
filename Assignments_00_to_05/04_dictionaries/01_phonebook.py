def main():
    # Initial phonebook (empty dictionary)
    phonebook = {}

    # Function to display the menu
    def display_menu():
        print("\nPhonebook Menu:")
        print("1. View all contacts")
        print("2. Add a contact")
        print("3. Lookup a contact")
        print("4. Delete a contact")
        print("5. Exit")

    # Main loop for the phonebook
    while True:
        display_menu()

        # Get the user's choice
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            # View all contacts
            print("\nPhonebook Contacts:")
            if not phonebook:
                print("Phonebook is empty.")
            else:
                for name, number in phonebook.items():
                    print(f"{name}: {number}")

        elif choice == "2":
            # Add a contact
            name = input("Enter the name of the new contact: ")
            number = input("Enter the phone number of the new contact: ")
            phonebook[name] = number
            print(f"Contact for {name} added successfully.")

        elif choice == "3":
            # Lookup a contact
            name = input("Enter the name to look up: ")
            if name in phonebook:
                print(f"{name}: {phonebook[name]}")
            else:
                print(f"Contact for {name} not found.")

        elif choice == "4":
            # Delete a contact
            name = input("Enter the name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact for {name} deleted successfully.")
            else:
                print(f"Contact for {name} not found.")

        elif choice == "5":
            # Exit the program
            print("Exiting phonebook...")
            break

        else:
            print("Invalid choice, please try again.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
