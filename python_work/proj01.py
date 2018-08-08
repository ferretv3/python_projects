######################################################
#PROJECT 1 - 5/13/2018
#1.takes input distance (rods)
#2.converts input into meters, furlongs, miles, and feet
#3.calculates time (minutes) to walk input distance
#4.outputs conversions and time to walk input distance  
######################################################

#1.INPUT

rods_float = float(input("Input rods: "))
print("You input",rods_float,"rods.")

#2.DISTANCE CONVERSIONS

meters_float = rods_float * 5.0292     #rods to meters conversion
furlongs_float = rods_float / 40       #rods to furlongs conversion
miles_float = meters_float / 1609.34   #meters to miles conversion
feet_float = meters_float / 0.3048     #meters to feet conversion

#3.WALKING TIME CALCULATION

MINUTES_PER_ROD = 1 / (3.1 / 60)          
    #(minutes/mile)
minutes_float = (MINUTES_PER_ROD * miles_float)  
    #(minutes/mile)*miles = total minutes

#4.OUTPUT
    
print("\nConversions")
print("Meters:",round(meters_float,3))
print("Feet:",round(feet_float,3))
print("Miles:",round(miles_float,3))
print("Furlongs:",round(furlongs_float,3))
print("Minutes to walk",rods_float,"rods: ",round(minutes_float,3))
    #round(x,3): rounds float to 3 decimal places