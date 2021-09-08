# loop function for tickets
# start of loop

name = ""
count = 0
max_tickets = 5

while name != "xxx" and count < max_tickets:
    print("You have {} seats "
          "left".format(max_tickets - count))

    # get details

    name = input("Name: ")
    count += 1
    print()

if count == max_tickets:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(count, max_tickets - count))

