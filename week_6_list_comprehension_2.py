# Print a list in which all the negative integers of the given list
# are replaced by their squares and all the positive numbers are left as it is.

def number():
    while True:
        userInput = input('Please enter a non-negative integer number: ')
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Input error.")