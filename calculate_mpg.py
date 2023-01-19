def main():

    start_odometer = int(input("Enter the starting odometer reading in miles: "))
    end_odometer = int(input("Enter the ending odometer reading in miles: "))
    fuel_amount = float(input("Enter the amount of fuel used in gallons: "))
    # Get an odometer value in U.S. miles from the user.

    # Get another odometer value in U.S. miles from the user.

    # Get a fuel amount in U.S. gallons from the user.

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_odometer, end_odometer, fuel_amount)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    # Display the results for the user to see.
    print(f'Your MPG is {mpg:.1f}')
    print(f'Your L/100K is {lp100k:.2f}')
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    miles_driven = float(end_miles) - float(start_miles)
    mpg = miles_driven / float(amount_gallons) 
    return mpg
    


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    l_per_100km = 235.215 / mpg # convert MPG to L/100km
    return l_per_100km
    
"""    
start_odometer = input("Enter the starting odometer reading in miles: ")
end_odometer = input("Enter the ending odometer reading in miles: ")
fuel_used = input("Enter the amount of fuel used in gallons: ") 

miles_driven = float(end_odometer) - float(start_odometer)
mpg = miles_driven / float(fuel_used) 

print("Miles per gallon: {:.2f}".format(mpg))
"""


# Call the main function so that
# this program will start executing.
main()