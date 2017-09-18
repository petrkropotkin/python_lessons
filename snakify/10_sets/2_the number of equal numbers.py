# Given two lists of numbers. Count how many unique numbers occur in both of them.
# This task can be solved in one line of code.
# hint:
# A & B
# A.intersection(B)
# Returns a set which is the intersection of sets A and B.

# 1 2 6 4 5 7
# 10 2 3 4 8            ==> 2


print(len(set(input().split()) & set(input().split())))