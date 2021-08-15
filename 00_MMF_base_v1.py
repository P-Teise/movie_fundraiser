

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


# ******* Main routine ***********

# <<<<<<< Loop to get ticket detail >>>>>>>>

    # Get name (can't be blank)
    name = not_blank("Name: ",
                 "Sorry - this can't be blank, "
                 "please enter your name")

