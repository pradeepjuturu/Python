# delcating formatter

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter %("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter %("I had this thing", 
"That ypu could type up right", 
"But It didn't sing", 
"So I said goodnight")

print "1 2 3 4"