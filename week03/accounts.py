# Weekly Task 03
# Author Gabriela Domiciano


# Account_number = 1234567890
# First start with 0 and not with 1

# Mask the first 6 digits with Xs and display the last 4 digits

# sources: Youtube Chanel PromoAmbitions- Python String Tutorial and w3schools



account_number_input = input("Enter the 10-character account number: ")
last_four_number = account_number_input[-4:]
print ('XXXXXX{}' .format (last_four_number))



# diferenbt length  

account_number_input = input("Enter the 5-character account number: ")
last_two_number = account_number_input[-2:]
print ('XXXXXX{}' .format (last_two_number))
       
