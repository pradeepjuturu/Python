#calling and importing argv function 
from sys import argv
#giving the details for argv. what it should input and declaring the script
script, filename = argv
#giving a word or variable to open the file using open() command
txt = open(filename)
#printing the name of the file
print "Here's your file %r:" %filename
#printing the details of the file using read() command
print txt.read()

#trying to reprint. printing the name of the file using raw_input() command
print "Type the filename again:"
#getting the raw_input for the file
file_again = raw_input(">")

#using a different text to open the file again.
txt_again = open(file_again)
#printing the contents of the file using read() command
print txt_again.read()
