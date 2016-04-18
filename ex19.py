
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses" %cheese_count
	print "You have %d boxes of crackers" %boxes_of_crackers
	print "why do you have so many of them"
	print "Arrange a party.\n"


print "We can give the function numbers directly"
cheese_and_crackers(50, 80)

print "Or, We can use variables from our script"
amount_of_cheese = 70
amount_of_crackers = 100

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we do math inside too"
cheese_and_crackers(10+50, 40+4)

print " we can combine them both, variables and math"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+99)

