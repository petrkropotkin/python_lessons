# In chess it is known that it is possible to place 8 queens on an 8×8 chess board
# such that none of them can attack another. Given a placement of 8 queens on the board,
# determine if there is a pair of queens that can attach each other on the next move.
# Print the word NO if no queen can attack another, otherwise print YES.
# The input consists of eight coordinate pairs, one pair per line,
#  with each pair giving the position of
# a queen on a standard chess board with rows and columns numbered starting at 1.

c = []
for i in range(8):
    a = [int(i) for i in input().split()]
    c.append(a)
 #c= [[1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1]]

flag = False


for i in range(len(c)):
    for j in range(i+1,len(c)):
        if abs(c[i][0] - c[j][0]) == abs(c[i][1] - c[j][1]) or c[i][0] == c[j][0] or c[i][1] == c[j][1]:
            flag = True

if flag:
    print('YES')
else: print('NO')





