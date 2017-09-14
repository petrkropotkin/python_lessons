# Chess rook moves horizontally or vertically. Given two different cells of the
# chessboard, determine whether a rook can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
# first two - for the first cell, and then the last two - for the second cell.
# The program should output YES if a rook can go from the first cell to the second in one move,
# or NO otherwise.
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

#Chess rook moves horizontally:
if x1 == x2:
    if y1 > y2 or y1 < y2:
        print("YES")

#Chess rook moves vertically:
elif y1 == y2:
    if x1 > x2 or x1 < x2:
        print("YES")
else:
    print("NO")


#======================================================

# answer from site
# if x1 == x2 or y1 == y2:
#     print("YES")
# else:
#     print("NO")
#=====================================================
