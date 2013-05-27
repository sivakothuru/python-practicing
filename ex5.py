name = "Siva Reddy.K"
age = 23
height = 180 / 2.54 # inches
weight = 71 * 2.2 # pounds
eyes = "Blue"
teeth = "white"
hair = "Black"

from math import ceil, floor

print "Let's talk abous %s." % name
print "He's %r inches tall." % ceil(height)
print "He's %r pounds heavy." % floor(weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the tea." % teeth

# this line is trikcy, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)