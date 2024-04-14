# Author Gabriela Domiciano Avellar
# Weekly Task 02

# Write a program called bank.py 
# The program should:
# Prompt the user and read in two money amounts (in cent)
# Add the two amounts
#Print out the answer in a human readable format 
# with a euro sign and decimal point between the euro and cent of the amount



amount1 = int(input("Enter amount1(in cent): "))
amount2 = int(input("Enter amount2(in cent): "))
result = (amount1 + amount2) / 100
print(f'The sun of these is €{result}')
