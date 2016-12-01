# Created on 22 Nov 2016
# Created by: Matthew Lourenco
# This is a program that creates a custom vehicle
# Edited on: 28 Nov 2016
# Fixed bug that prevents it from working in python 2.7
# Edited on: 1 Dec 2016
# gave functionality to setters other than just changing the numbers

from vehicle import *

#create a vehicle
car1 = Vehicle()
car2 = Vehicle()

print('Car 1:')
car1.set_license_plate_number('7letter')
print('Speed: ' + str(car1.get_speed()) + 'km/h')
car1.set_gear(3)
car1.set_gear(5)
car1.set_gear(7)
car1.brake(50)
car1.brake(100)

print('\nCar 2:')
car2.set_license_plate_number('7letter')
print('Paint colour: ' + str(car2.get_colour()))
car2.set_license_plate_number('7things')
car2.set_colour('nil')
car2.set_license_plate_number('8letters')
car2.set_colour('red')
