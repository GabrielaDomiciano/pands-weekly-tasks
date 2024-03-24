# Gabriela Domiciano
# Write a program that outputs whether or not today is a weekday.
# sources: weebsite: Tutorials point, SheCodes.


import datetime

def is_weekday():
    
    today = datetime.datetime.today()  # Get the today date
    
    day_of_week = today.weekday()  # Get the week day (0 Monday, 1 Tuesday etc)
    
    return day_of_week < 5  # Check if is a weekday (Monday to Friday)

if __name__ == "__main__":
    if is_weekday():
        print("Yes, unfortunately today is a weekday.")
    else:
        print("It is the weekend, yay!")