# Gabriela Domiciano
# collatz

number = int(input("enter number: "))
#numbers = [number]

while number != 1 :
    if (number % 2) == 0: # If Even
        number = number //2
        #numbers.append(number)
        print (number)

    else: # Se Odd
        number = number *3 +1
        #numbers.append(number)
        print (number)
    
#print(numbers)
