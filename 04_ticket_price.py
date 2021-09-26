profit = 0

name = ""
while name != "xxx":

    name = input("Name: ")   # replace with function call

    # If name is exit code, break out of the loop
    if name == "xxx":
        break

    age = int(input("Age: "))   # replace with function

    if age < 16:
        ticket_price = 7.50
    elif age >= 65:
        ticket_price = 6.50
    else:
        ticket_price = 10.50

    profit_made = ticket_price - 5
    profit += profit_made

    print("{} : ${:.2f}".format(name, ticket_price))

print("Profit from ticket: ${:.2f}".format(profit))


