#hard
# Given two positive integers mm and nn, mm lines of n elements,
# giving an m×n matrix A, followed by two non-negative integers
# i and j less than nn, swap columns i and j of A and print the result.
# Write a function swap_columns(a, i, j) and call it to exchange the columns.
# input:
# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 0 1

# output:
# 12 11 13 14
# 22 21 23 24
# 32 31 33 34

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]


def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]


    for row in a:
        print(' '.join([str(elem) for elem in row]))


swap_columns(a, i, j)












