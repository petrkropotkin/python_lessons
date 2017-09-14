#a)
# the first line of input is the number of rows of the array
n = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
print(a)

#b)
# the first line of input is the number of rows of the array
n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
print(a)

#c)
a = [list(map(int,input().split())) for i in range(int(input()))]

#d)
a = [[int(j) for j in input().split()] for i in range(int(input()))]
