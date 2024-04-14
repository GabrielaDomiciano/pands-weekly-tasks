# Author Gabriela Domiciano
# Weekly Task 03

# Write a python program called accounts.py that reads in a 10 character account number 
# and outputs the account number with only the last 4 digits
# showing (and the first 6 digits replaced with Xs).

# Account_number = 1234567890
# First start with 0 and not with 1

# Mask the first 6 digits with Xs and display the last 4 digits

# sources: Youtube Chanel PromoAmbitions- Python String Tutorial and w3schools



account_number = input("Enter the 10 character account number: ")
last_four_number = account_number[-4:]
print ('XXXXXX{}' .format (last_four_number))


# diferenbt account number

account_number = input("Enter the 5 character account number: ")
last_two_number = account_number[-2:]
print ('XXXXXX{}' .format (last_two_number))
       
