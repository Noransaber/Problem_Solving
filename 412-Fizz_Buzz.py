#!/usr/bin/python3
"""
This module creates a 1-indexed list, based on the following criteria:
- answer[i] == "FizzBuzz" if i is divisible by 3 and 5
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.
"""


def fizzbuzz():
    import sys

    number_of_trials = 1

    # This block determines the number of tries user has to input correct val
    # It does this with the help of number_of_trials
    while (number_of_trials <= 3):
        user_input = input("Please enter a valid integer value: ")

        # Checks if value entered by user doesen't contain letters
        if user_input.isnumeric():
            user_input = int(user_input)

        # if it's a valid integer it breaks out of the while loop
        if (
                (type(user_input) is int) and
                (user_input is not bool) and
                (1 >= user_input <= 10**4)
           ):
            break
        # if it isn't prompts user with appropriate message
        if number_of_trials != 3:
            print("Please enter an integer greater than 1"
                  " and less than 10000")
        if number_of_trials == 2:
            print("YOU HAVE ONE MORE TRIAL")
        elif number_of_trials == 3:
            print("Exiting...")
            sys.exit(1)

        # increment number of trials
        number_of_trials += 1

    # initializing an empty list to hold the new list
    fizz_list = []

    # because our list is 1-indexed we increment by 1
    for i in range(user_input + 1):
        if i == 0:
            continue
        if (((i % 3) == 0) and ((i % 5) == 0)):
            fizz_list.append("FizzBuzz")
        elif ((i % 3) == 0):
            fizz_list.append("Fizz")
        elif ((i % 5) == 0):
            fizz_list.append("Buzz")
        else:
            fizz_list.append(str(i))

    print(fizz_list)


if __name__ == "__main__":
    fizzbuzz()
