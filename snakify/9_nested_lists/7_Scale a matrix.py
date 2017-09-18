# easy
# Given two positive integers m and n, m lines of n elements, giving an m×n matrix A,
# followed by one integer c, multiply every entry of the matrix by c and print the result.
# input:
# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 2

# output:
# 22 24 26 28
# 42 44 46 48
# 62 64 66 68

m,n = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
c = int(input())

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] *= c


for row in a:
    print(' '.join([str(elem) for elem in row]))

