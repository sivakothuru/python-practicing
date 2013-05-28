# two argument function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# calling function
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# assigning values to the arguments
amount_of_cheese = 10
amount_of_crackers = 50

# calling function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# calling function
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# calling function where we are adding some values to the existing arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def names_and_marks(name, clas, marks):
    print "His is %r" % name
    print "He is studying %r class" % clas
    print "He secured %d marks" % marks
    print "This is his data\n"


print "I am passing three aeguments"
names_and_marks("siva reddy", "10th", 89)

mark = 90
print "I'm passing only two arguments and the third is intialised"
names_and_marks("sivareddy", "10th", mark) 

name = "sivareddy"
clas = "9th"
marks = 87
print "Here all the three are initialised before"
names_and_marks(name, clas, marks)

print "Here value is added to the already initialised values"
names_and_marks(name, clas, marks + 5)