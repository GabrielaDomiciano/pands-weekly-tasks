# Gabriela Domiciano
# Weekly Task 05

# Write a program that outputs whether or not today is a weekday.
# sources: Youtube Chanel:  Tutorials point, SheCodes.


import datetime

def is_weekday():
    
    today = datetime.datetime.today()  
    
    day_of_week = today.weekday() 
    
    return day_of_week < 5  

if __name__ == "__main__":
    if is_weekday():
        print("Yes, unfortunately today is a weekday.")
    else:
        print("It is the weekend, yay!")