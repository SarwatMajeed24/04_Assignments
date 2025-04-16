# # Define the speed of light as a constant
# SPEED_OF_LIGHT = 299792458

# def calculate_energy(mass_kg):
#     """Calculates the equivalent energy of a given mass using E=mc^2."""
#     energy_joules = mass_kg * (SPEED_OF_LIGHT ** 2)
#     return energy_joules

# def main():
#     """Prompts the user for mass and outputs the equivalent energy."""
#     print("Einstein's Mass-Energy Equivalence Calculator")
    

#     while True:
#         mass_input = input("Enter kilos of mass: ")
#         if mass_input.lower() == 'quit':
#             break

#         try:
#             mass = float(mass_input)
#             if mass < 0:
#                 print("Mass cannot be negative. Please enter a non-negative value.")
#                 continue

#             energy = calculate_energy(mass)
#             print("e = m * C^2...")
#             print(f"m = {mass} kg")
#             print(f"C = {SPEED_OF_LIGHT} m/s")
#             print(f"{energy} joules of energy!")
#             print("Enter 'quit' to exit.")

#         except ValueError:
#             print("Invalid input. Please enter a valid number for mass or 'quit'.")

# if __name__ == "__main__":
#     main()


# Define the speed of light as a constant
SPEED_OF_LIGHT = 299792458

def calculate_energy(mass_kg):
    """Calculates the equivalent energy of a given mass using E=mc^2."""
    energy_joules = mass_kg * (SPEED_OF_LIGHT ** 2)
    return energy_joules

def main():
    """Continually prompts the user for mass and outputs the equivalent energy with continue/exit option."""
    print("Einstein's Mass-Energy Equivalence Calculator")

    while True:
        mass_input = input("Enter kilos of mass: ")
        if mass_input.lower() == 'e':
            break

        try:
            mass = float(mass_input)
            if mass < 0:
                print("Mass cannot be negative. Please enter a non-negative value.")
                continue

            energy = calculate_energy(mass)
            print("e = m * C^2...")
            print(f"m = {mass} kg")
            print(f"C = {SPEED_OF_LIGHT} m/s")
            print(f"{energy} joules of energy!")

            choice = input("Enter 'e' to exit or 'c' to continue: ").lower()
            if choice == 'E':
                break
            elif choice == 'C':
                continue
            else:
                print("Invalid choice. Continuing...")

        except ValueError:
            print("Invalid input. Please enter a valid number for mass or 'e' to exit.")

if __name__ == "__main__":
    main()