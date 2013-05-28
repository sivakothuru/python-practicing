print "Let's practice everything"
# escape sequence characters
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'

# printing multiple lines
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""

print "--------------"
print poem

print "--------------"

# arith matic operation
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# function with arithmatic operations and a return function
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# calling function
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# another calling function
print "We'd have %d beans, %d jars, and %d crates" % secret_formula(start_point)