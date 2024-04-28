# Author Gabriela Domiciano Avellar
# Weekly Task 02
# Sources: Classes videos about Statements

# Write a program called bank.py 
# The program should:
# Prompt the user and read in two money amounts (in cent)
# Add the two amounts
#Print out the answer in a human readable format 
# with a euro sign and decimal point between the euro and cent of the amount



amount1 = int(input("Enter amount1(in cent): "))
# the user enter two amounts (in cents) and stores them as integers
amount2 = int(input("Enter amount2(in cent): "))
# sum these amounts and divides by 100 
result = (amount1 + amount2) / 100
print(f'The sun of these is €{result}')
