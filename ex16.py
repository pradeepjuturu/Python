#calling and importing argv function
from sys import argv
#giving the name of the currnt file and giving an input for argv
script, filename = argv
#printing if we want to earse or keep the details of the file
print "We are going to erase file %r" %filename
#asking if you want to erase or not. CTRL-C is a commnad that stops the code, means no
print "if you don't want that, hit CTRL-C (^C)"
#asking enter/return means yes and continue
print "If you do want that, hit RETURN"

#getting the answer for the above question by using raw_input command
raw_input("?")

print "opening the file..."
#using a variable to open the file. This is a new file. in python we can just use open() function to open and at the same time create the file.
#using 'w' means to open the file in write mode. we can use 'r' to open in read mode.
target = open(filename, 'w')
#just declaring what just happend
print "Truncating the file, goodbye"
#just erasing the details in the file. if there are any.
target.truncate()
#asking for input
print "Now I am going to ask you for three lines"
#taking the inputs using the raw_input command. This is just inputting in python not the file yet.
line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

#declaring what it is supposed to be doing
print "I am going to write these to the file "

#writing the lines using write() function
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it"
#closing the file
target.close()