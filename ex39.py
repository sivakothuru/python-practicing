# state abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#city abbreviations
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# adding more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# printing some cities

print "-" * 10
print "NY State has: ", cities["NY"]
print "OR State has: ", cities["OR"]

# printing some states
print "-" * 10
print "Michigan's abbreviation is: ", states["Michigan"]
print "Florida's abbreviation is: ", states["Florida"]

# doing it by using state then cities dict

print "-" * 10
print "Michigan has: ", cities[states["Michigan"]]
print "Florida has: ", cities[states["Florida"]]

#printing every state abbreviation

print "-" * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print "-" * 10
# safely getting  a abbreviation by state that might not be there
state = states.get("Texas", None)

if not state:
    print "Sorry, no Texas"

#getting city with a default value
city = cities.get("TX", "Does not exist")
print "The city for the state 'TX' is: %s" % city