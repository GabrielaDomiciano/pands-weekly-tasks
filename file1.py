#Gabriela Domiciano Avellar
# Weekly Task 07

#Counting how many letters E in the TXT file "moby_dick.txt"
#This code will convert the letter E to lowercase, to ensure that both 'E' and 'e' are counted.

#sources: Youtube Chanel: Cabral Engineering, Hashtag Programacao

'''
In the weekly_task description it is asked to get an argument on the command line, 
I didn't understand if it was to create a txt file as explained in the class, inside of
the week07 folder, or if it was to put a sentence on a line and make the code

'''

# open file file 2: I created the file2 using a text in a command line as a base.

with open("moby_dick.txt", "r") as file:
    lines = file.readlines()

quantity = 0

for line in lines:
    for letra in line:
        if letra.lower() == "e":
            quantity += 1

print('In the text file "moby_dick.txt", there are', quantity, 'letters "E".')       






