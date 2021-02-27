'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
whole = input("Please enter a whole number for conversion: ")
whole = int(whole)
whole = float
print (whole)

decimal = input("Please enter a number with a decimal for conversion: ")
decimal = float(decimal)
decimal = int
print(decimal)

whole = input("Please enter a first number for division: ")
whole = int(whole)
decimal = input("Please enter a second number for division: ")
decimal = int(decimal)
print(whole / decimal)


whole = input("Please enter a first number for multiplication: ")
whole = int(whole)
decimal = input("Please enter a second number for multiplication: ")
decimal = int(decimal)
print(whole * decimal)