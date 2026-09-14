# mini project: movie ticket pricing
# 1. define a variable called age, assign any value for it
# 2. using conditional statement to set up different age have different pricing
# condition (1): age less than or equal to 18 - RM10
# condition (2): age between 19 TO 59 - RM20
# condition (3): age greater than or equal to 60 - RM12

# solution 1: with input() and using 'and' for between range value
age = int(input("Enter your age: "))
if age <= 18:
    print("Ticket Price: RM10")
elif age >= 19 and age <= 59:
    print("Ticket Price: RM20")
else:
    print("Ticket Price: RM12")

# solution 2: direct assign value to age variable
age = 18
if age <= 18:
    print("Ticket Price: RM10")
elif age >= 19 and age <= 59:
    print("Ticket Price: RM20")
else:
    print("Ticket Price: RM12")

# solution 3: use comparison operators 
age = 18
if age <= 18:
    print("Ticket Price: RM10")
elif 19 <= age <= 59::
    print("Ticket Price: RM20")
else:
    print("Ticket Price: RM12")
