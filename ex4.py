#declaring the details
cars = 100
Space_in_a_car = 4.0
drivers = 30
passengers = 90
#calculating the details using the data
Cars_not_driven = cars-drivers
cars_driven = drivers
Carpool_capacity = cars_driven * Space_in_a_car
average_passengers_per_car = passengers/cars_driven

#printing the calculated data
print "There are", cars, "cars in the lot"
print "There are", drivers, "available"
print "The number of cars driven", cars_driven
print "The Carpool Capacity", Carpool_capacity
print "Average Passengers per car", average_passengers_per_car