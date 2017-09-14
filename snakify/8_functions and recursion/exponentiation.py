# Given a positive real number aa and a non-negative integer n.
# Calculate anan without using loops, ** operator or the built in function math.pow().
# Instead, use recursion and the relation a**n=a*a**n−1. Print the result.
# Form the function power(a, n).
def expo_rec(a,n):

    if n == 0:
        return 1
    else:
        return a*expo_rec(a,n-1)

print(expo_rec(2,1))

