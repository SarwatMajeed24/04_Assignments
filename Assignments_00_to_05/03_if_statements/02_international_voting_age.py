def main():
    """Asks the user for their age and checks voting eligibility in fictional countries using if-else."""

    try:
        age = int(input("How old are you? "))

        peturksbouipo_age = 16
        stanlau_age = 25
        mayengua_age = 48

        print("Voting Eligibility:")

        if age >= peturksbouipo_age:
            print(f"You can vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")
        else:
            print(f"You cannot vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")

        if age >= stanlau_age:
            print(f"You can vote in Stanlau where the voting age is {stanlau_age}.")
        else:
            print(f"You cannot vote in Stanlau where the voting age is {stanlau_age}.")

        if age >= mayengua_age:
            print(f"You can vote in Mayengua where the voting age is {mayengua_age}.")
        else:
            print(f"You cannot vote in Mayengua where the voting age is {mayengua_age}.")

    except ValueError:
        print("Invalid input. Please enter a whole number for your age.")

if __name__ == "__main__":
    main()