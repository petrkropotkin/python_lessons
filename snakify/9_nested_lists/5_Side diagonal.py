# Hard
# Given an integer n, create a two-dimensional array of size (n×n)
# and populate it as follows, with spaces between each character:
# The positions on the minor diagonal (from the upper right to the lower left corner) receive 1.
# The positions above this diagonal recieve 0 .
# The positions below the diagonal receive 2 .
# Print the elements of the resulting array.

n = int(input())
a = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if j == n - i - 1:
            a[i][j] = 1
        if j > n - i - 1:
            a[i][j] = 2

for row in a:
    print(' '.join([str(elem) for elem in row]))

# -----------Suggested solution---------------------

n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2


for row in a:
    for elem in row:
        print(elem, end=' ')
    print()