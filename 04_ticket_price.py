profit = 0

name = ""
while name != "xxx":

    name = input("Name: ")   # replace with function call

    # If name is exit code, break out of the loop
    if name == "xxx":
        break

    age = int(input("Age: "))   # replace with function

    if age < 16:
        print("That ticket costs $7.50")
    elif age >= 65:
        print("That ticket costs $6.50")
    else:
        print("That ticket costs $10.50")



