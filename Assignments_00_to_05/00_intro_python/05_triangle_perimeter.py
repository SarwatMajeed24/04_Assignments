
   # Prompts the user for the lengths of the three sides of a triangle
   # and calculates and prints its perimeter.
    
def calculate_triangle_perimeter():
    
    try:
        side1_str = input("What is the length of side 1? ")
        side1 = float(side1_str)

        side2_str = input("What is the length of side 2? ")
        side2 = float(side2_str)

        side3_str = input("What is the length of side 3? ")
        side3 = float(side3_str)

        perimeter = side1 + side2 + side3
        print(f"The perimeter of the triangle is {perimeter}")

    except ValueError:
        print("Invalid input. Please enter valid numbers for the side lengths.")

if __name__ == "__main__":
    calculate_triangle_perimeter()