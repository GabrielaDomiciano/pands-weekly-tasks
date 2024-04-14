# Author: Gabriela Domiciano Avelar
# Weekly Task 06

# Write a program that takes
# a positive floating-point number as input and outputs an approximation of its square root.

def apx(number):
    if number < 0:
        return "Dont acept negative number"

    if number == 0:
        return 0

    guess = number / 2
    epsilon = 0.000001  # Tolerance level for approximation

    while True:
        new_guess = (guess + number / guess) / 2
        if abs(new_guess - guess) < epsilon:
            return new_guess
        guess = new_guess

def main():
    input_number = float(input("Enter a positive number: "))
    result = apx(input_number)
    print("Approximation of square root:", result)

if __name__ == "__main__":
    main()