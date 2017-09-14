# Given a sequence of integers that end with a 00. Print the sequence in reverse order.
# Don't use lists or other data structures. Use the force of recursion instead.

def reverse():
    n = int(input())

    if n != 0:
        reverse()

    print(n)



#
# reverse()
#
#
# def reverse():
#     x = int(input())
#
#     if x != 0:
#         reverse()
#
#     print(x)

print(reverse())
