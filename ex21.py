# addition function
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

# substarction function
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

# multiplication function
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

# division function
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

# calling functions
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# calling  multiple functions by passing one function as a argument to another function
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


inverse_value = divide(age, multiply(height, subtract(weight, add(iq, 1))))

print "That becomes: ", inverse_value, "This is the inverse of the above function"
value = 35 + 74 - 180 * 50 / 2
print value