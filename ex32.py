the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pineapples", "pappayas"]
change = [1, "pennies", 2, "dimes", 3, "quaters"]

# first for-loop
for number in the_count:
    print "This is count %d" % number

# second for for-loop
for fruit in fruits:
    print "A fruiot of type: %s" % fruit

# third for-loop working on mixed lists
for i in change:
    print "I got %r" % i

# buliding lists
elements = []

# for-loopusing range function
for i in range(0, 6):
    print "Adding %d to the list" % i
    # append operation on list
    elements.append(i)

# printing elements in the appended list
for i in elements:
    print "Elements was: %d" % i