#easy
# Given two integers representing the rows and columns (m×n)
# , and subsequent mm rows of nn elements, find the index position
# of the maximum element and print two numbers representing the index
# (i×j) or the row number and the column number. If there exist multiple
# such elements in different rows, print the one with smaller row number.
# If there multiple such elements occur on the
# same row, output the smallest column number.

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
print(a)
maxi = a[0][0]
maxi_i = 0
maxi_j = 0

for i in range(n):
    for j in range(m):
        if a[i][j] > maxi:
            maxi = a[i][j]
            maxi_i,maxi_j = i,j
print(maxi_i,maxi_j)


