#initializing number of cars
cars = 100
#initializing space in a cars
space_in_a_car = 4.0
#number of drivers
drivers = 30
#  number of passengers
passengers = 90
# cars that dont have drivers
cars_not_driven = cars - drivers
#number of cars having drivers
cars_driven = drivers
# total capacity of all cars collectively
carpool_capacity = cars_driven * space_in_a_car
#average passengers per a car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"