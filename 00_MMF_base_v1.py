# Functions go here
# check that ticket holder name is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        # if input is not blank, program continues
        if response != "":
            return response

        # if input is blank, display error message (& loop until there is correct input)

        else:
            print(error_message)


# checks for an integer more than 0
def int_check(question):
    error = "Please enter a whole number between 12 " \
            "and 130"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if integer is not entered, display an error message
        except ValueError:
            print(error)


# ******* Main routine ***********

# <<<<<<< Loop to get ticket detail >>>>>>>>
# start of loop
# initialise loop so that it runs at least once

# Get name (can't be blank)
MAX_TICKETS = 5
name = ""
ticket_count = 0
ticket_sales = 0

while name != "xxx" and ticket_count < MAX_TICKETS:

    # tells user how many seats are left
    if ticket_count == MAX_TICKETS:
        print("You have sold all the available tickets!")

    # tells user how many tickets have been sold and how many tickets are left
    elif ticket_count < MAX_TICKETS - 1:
        print("You have sold {} tickets. You have {} places available".format(ticket_count, MAX_TICKETS - ticket_count))
    # warns user only ONE seat is left
    else:
        print("You have 1 seat left")

    # Get details...
    name = not_blank("Name: ", "Please enter your name")

    # end of loop if exit code is input
    if name == "xxx":
        break

    # Get age (between 12 and 130)
    age = int_check("Age: ")

    # check that age is valid ...
    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue

    if age < 16:
        ticket_price = 7.50
    elif age >= 65:
        ticket_price = 6.50
    else:
        ticket_price = 10.50

    ticket_count += 1
    ticket_sales += ticket_price

# End of tickets loop

# calculate profits etc.
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))
