ten_things = "Apples Oranges Telephones Light Sugar"

print "Wait there's not 10 things in that list, let's fix them"

# split the sentence into list bases on the content in thae string(space here                                                                                       )
stuff = ten_things.split(" ")
more_stuff = ["Days", "Nights", "Song", "Frisbee","Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print "There's %d items now" % len(stuff)

print "There we go:", stuff
print "Let's do somethings with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print " ".join(stuff)
