# Gabriela Domiciano Avellar
# Weekly Task 04

# Write a program, called collatz.py, that asks the user to input 
# any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even,
# divide it by two, but if it is odd, multiply it by three and add one.

# sources: https://www.geeksforgeeks.org/program-to-print-collatz-sequence/
#          https://www.programiz.com/python-programming/while-loop          


number = int(input("enter number: "))

#  The loop stops when the number becomes 1
# at the point the conditionis no longer met, and the loop stops.
while number != 1 :
    if (number % 2) == 0: 
        # removes any decimal part
        number = number //2
        #numbers.append(number)
        print (number)

    else:
        number = number *3 +1

        print (number)
    

