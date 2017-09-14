#easy
# Given an odd number integer n, produce a two-dimensional array of size (n×n).
# Fill each element with a single character string of "." .
# Then fill the middle row, the middle column and the diagnals with the single character string of "*"
# (an image of a snow flake). Print the array elements in (n×n) rows and columns and separate
# the characters with a single space.
n = int(input())
a = [['.'] * n for i in range(n)]
middle = len(a)//2

# my guesses :
# column j == middle
# row i = middle

# main diagonal i==j
# secondary diagonal j == len(a) - i - 1

for i in range(len(a)):
    for j in range(len(a[i])):
        if j == middle or i == middle or i==j or j == len(a) - i - 1:
            a[i][j] = '*'

for row in a:
    print(' '.join(row))

#==============Suggested solution==============================
n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))