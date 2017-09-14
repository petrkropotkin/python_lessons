# Chocolate bar has the form of a rectangle divided into n×mn×m portions.
# Chocolate bar can be split into two rectangular parts by breaking it along
# a selected straight line on its pattern. Determine whether it is possible to
# split it so that one of the parts will have exactly k squares.
# The program reads three integers: n, m, and k. It should print YES or NO

#------------------ The solution----------------------------------:

# the number K is should be a multiple of one or the width, or the length
# and should be less than the total number of pieces

n = int(input())
m = int(input())
k = int(input())

if k < (n * m) and k % n == 0 or k % m == 0 :
    print('YES')
else:
    print('NO')



