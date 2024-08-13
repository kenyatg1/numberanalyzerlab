def display_result(value):
    if 1 <= value <= 10:
        print("The number is between 1 and 10.")
    elif 11 <= value <= 20:
        print("The number is between 11 and 20.")
    elif 21 <= value <= 30:
        print("The number is between 21 and 30.")
    elif 31 <= value <= 40:
        print("The number is between 31 and 40.")
    elif 41 <= value <= 50:
        print("The number is between 41 and 50.")
    elif 51 <= value <= 60:
        print("The number is between 51 and 60.")
    elif 61 <= value <= 70:
        print("The number is between 61 and 70.")
    elif 71 <= value <= 80:
        print("The number is between 71 and 80.")
    elif 81 <= value <= 90:
        print("The number is between 81 and 90.")
    elif 91 <= value <= 100:
        print("The number is between 91 and 100.")
    else:
        print("The number is out of range.")

# Main program
try:
    user_input = int(input("Enter an integer between 1 and 100 inclusive: "))
    if 1 <= user_input <= 100:
        display_result(user_input)
    else:
        print("Error: The number is not between 1 and 100.")
except ValueError:
    print("Error: Please enter a valid integer.")
