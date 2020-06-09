# Three integers P, Q and R represent the dimensions of a cuboid.
# Print a list of all possible coordinates given by i, j, k on a 3D grid
# where the sum of (i + j + k) is not equal to N.
# 0 <= i <= P; 0 <= j <= Q; 0 <= k <= R
# Print the list in lexicographic increasing order.

def number():
    while True:
        userInput = input('Please enter a non-negative integer number: ')
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Input error.")


result = []
p = number()
q = number()
r = number()
n = number()

result = [[i, j, k] for i in range(p + 1) for j in range(q + 1) for k in range(r + 1) if i + j + k != n]
print(result)