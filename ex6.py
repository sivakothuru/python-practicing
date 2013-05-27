# inserting integer into a string
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
# inserting string in middle of other string
y = "Those eho know %s and those who %s" % (binary, do_not)

print x
print y
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# inserting string in middle of another string
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side"
# adding two strings
print w + e