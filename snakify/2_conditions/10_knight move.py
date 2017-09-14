# Chess knight moves like the letter L. It can move two cells horizontally and one
# cell vertically, or two cells vertically and one cells horizontally.
# Given two different cells of the chessboard,
# determine whether a knight can go from the first cell to the second in one move.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) == 2 and abs(y1 - y2) == 1 :
    print('YES')
elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2 :
    print('YES')

else:
    print('NO')

