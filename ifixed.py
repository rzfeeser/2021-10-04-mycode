#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""

while (calc1 != "q"):
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input()
    
    # if the user put in anything that is NOT numeric, QUIT
    if not calc1.isnumeric():
        break

    calc1 = float(calc1) # calc1 will ALWAYS be a numeric value we can take the float of


    print("\nWhat is the second operator? Or, enter q to quit: ")
    
    calc2 = input()

    # again, you gave us something that is not a number, so QUIT
    if not calc2.isnumeric():
        break
    
    calc2 = float(calc2)


    print("Enter an operation to perform on the two operators (+ or -): ")
    
    operation = input()
    
    if operation == "+":
        print(f"\n{calc1} + {calc2} = {calc1 + calc2}")
    elif operation == '-':
        print(f"\n {calc1} + {calc2} {calc1 - calc2}")
    else:
        print("\n Not a valid entry. Restarting...")
