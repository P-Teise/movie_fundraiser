# loop function for tickets
# start of loop

name = ""
count = 0
max_tickets = 5

while name != "xxx" and count < max_tickets:


    # get details

    name = input("Name: ")
    count += 1
    print()

    if count == max_tickets:
        print("You have sold all the available tickets!")
    # tells user how many tickets have been sold and how many tickets are left
    elif count < 4:
        print("You have sold {} tickets. \n"
              "There are {} places still available"
              .format(count, max_tickets - count))
    # grammar corrected to emphasize only ONE seat is left
    else:
        print("You have sold 4 tickets. \n"
            "You have 1 seat left")


