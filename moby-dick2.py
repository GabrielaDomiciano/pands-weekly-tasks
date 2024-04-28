#Author GAbriela Domiciano Avellar
## Weekly Task 07

#Counting how many letters E in the TXT file "moby_dick.txt"
#This code will convert the letter E to lowercase, to ensure that both 'E' and 'e' are counted.

#sources: Youtube Chanel: Cabral Engineering, Hashtag Programacao.
'''
In the weekly_task description it is asked to get an argument on the command line, 
I didn't understand if it was to create a txt file as explained in the class, inside of
the week07 folder, or if it was to put a sentence on a line and make the code

'''
# open moby-dick1: I created the moby-dick1  using a txt file as a reference.


moby_dick = 'Better to sleep with a sober cannibal than a drunk  Christian'
Qt= 0
for letter in moby_dick : 
    if letter.lower() == 'e':
       Qt = Qt + 1
print('in the text file', moby_dick, 'there are', Qt, 'letters E')