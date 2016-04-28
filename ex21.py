def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a+b

def subtract(a, b):
	print "Subtracting %d - %d" %(a, b)
	return a-b

def multiply(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a*b
	
def divide(a, b):
	print "Dividing %d / %d" % (a, b)
	return a/b
	
print "Let's do some math just with functions"

age = add(25, 5)
height = subtract(78, 15)
weight = multiply(85, 2)
iq = divide(250, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %r" % (age, height, weight, iq)

# A puzzle for extra credit

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes", what, "Can you do it by hand"