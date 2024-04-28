# Gabriela Domiciano
# Weekly Task 05

# Write a program that outputs whether or not today is a weekday.
# sources: Youtube Chanel:  Tutorials point, SheCodes.


import datetime
# It defines a function that checks if the current day is a weekday.
# 0 for Monday, 1 for Tuesday, ..., 6 for Sunday
def is_weekday():
    
    today = datetime.datetime.today()  
    day_of_week = today.weekday() 
    return day_of_week < 5  
# It returns True if the day of the week is less than 5

if __name__ == "__main__":
    if is_weekday():
        print("Yes, unfortunately today is a weekday.")
    else:
        print("It is the weekend, yay!")