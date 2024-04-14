# Author: Gabriela Domiciano Avelar
# Weekly Task 06

# Write a program that takes
# a positive floating-point number as input and outputs an approximation of its square root.

#sources: Weeb Site- https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

def sqrt(number):
    if number < 0:
        return "Don't accept negative number"

    if number == 0:
        return 0 #  0 = 0

    x = number
    # root = 0.5 * (X + (N / X))
    tolerance = 0.00001

    while True:
        print(" x = ", x)
        root = 0.5 * (x + (number/x))
        print("root=", root)
        if (abs(root - x) < tolerance) :
            break
        x = root

    return root 

number = float(input("Please enter a positive number: "))
result = sqrt(number)
print(f"The square root of {number} is approx. {result}")



