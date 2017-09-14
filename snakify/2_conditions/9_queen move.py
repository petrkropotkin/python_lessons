# Chess queen moves horizontally, vertically or diagonally to any number of cells. Given
# two different cells of the chessboard,
# determine whether a queen can go from the first cell to the second in one move.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) == abs(y1 - y2) :
    print('YES')

elif x1 == x2 :
    print('YES')
elif y1 == y2 :
    print('YES')

else:
    print('NO')
