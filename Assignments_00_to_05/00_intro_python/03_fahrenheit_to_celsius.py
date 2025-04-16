
    #Prompts the user for a temperature in Fahrenheit and outputs
    #the equivalent temperature in Celsius.
    
def fahrenheit_to_celsius():
 
    try:
        fahrenheit_str = input("Enter temperature in Fahrenheit: ")
        degrees_fahrenheit = float(fahrenheit_str)
        degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
        print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")
    except ValueError:
        print("Invalid input. Please enter a valid number for the temperature.")

if __name__ == "__main__":
    fahrenheit_to_celsius()