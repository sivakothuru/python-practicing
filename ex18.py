# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# double arguments
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# single argument
def print_one(arg1):
    print "arg1: %r" % arg1

# no arguments
def print_none():
    print "I got nothin'."


print_two("Siva","Reddy")
print_two_again("Siva","Reddy")
print_one("First")
print_none()