#delcaring and importing argv and exists functions
from sys import argv
from os.path import exists

#input declaration for argv
script, from_file, to_file = argv

#declaring the copying files and from & to
print "Copying form %s to %s" %(from_file, to_file)

#opening the from file using a variable
in_file = open(from_file)
# reading the from file by using the previously delcared variable in-file and storing in the new variable indata
indata = in_file.read()

#Giving the size of the variable by using len() function
print "The input file is %d bytes long" % len(indata)

#checking if the to_file exits or not by using exists function
print "Does the output file exists %r " %exists(to_file)

#checking if still want to do it or abort the task
print "Ready, hit RETURN to continue or CTRL-C to abort"
#taking the input by using raw_input 
raw_input()

#opening the file in write mode using open() function  and storing it in a variable out_file
out_file = open(to_file, 'w')
#writng in the out_file variable the indata
out_file.write(indata)

print "All done"
#closing the files
out_file.close()
in_file.close()
