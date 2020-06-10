# Print a list in which all the negative integers of the given list
# are replaced by their squares and all the positive numbers are left as it is.


def numbers():
    userInput = input('Please enter a few integer numbers (positive and negative) separated by spaces: ').split()
    for i in range(len(userInput)):
        try:
            userInput[i] = int(userInput[i])
        except ValueError:
            print("\nOops!  Something went wrong.\n")
            numbers()
    return userInput


result = [x if x > 0 else x * x for x in numbers()]

print(result)