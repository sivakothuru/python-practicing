people = 30
cars = 40
buses = 15
# if cars greater than people then the print statement will get executed
if cars > people:
    print "We should take the cars."
elif cars < people:             # if cars less than people then the print statement will get executed
    print "We should not take the cars."
else:                           # if both the conditions are false then else is exicuted
    print "We can't decide"

if buses > cars:                # if buses greater than cars then the print statement will get executed
    print "That's too many buses"
elif buses < cars:              # if buses less than cars then the print statement will get executed
    print "May be we could take the busses"
else:                           # if "if" and "elif" fails this will get exicuted
    print "We still cant decide"

if people > buses:              # if people greater than buses then the print statement will get executed
    print "Alright, let's just take the buses"
else:                           # if conditions fails then this will get executed
    print "Fine, let's stay home then"

if cars > people and buses < cars: # if cars greaterthan people and buses lessthan cars then this will get executed
    print "Too many cars"
elif cars < people and buses > cars:# if cars lessthan people and buses greaterthan cars then this will gwt executed
    print "Better to take buses"
else:                                # if the above two conditions fails then this will get executed
    print "Let's stay in  home"
