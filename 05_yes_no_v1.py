def yes_no(question):

    error = "Please answer yes / no"

    valid = false
    while not valid:

        # ask question and put response in lower case
        response = input(question).lower()

        if response == "Yes":
            return response
        elif response == "Y":
            return response
        elif response == "No":
            return response

