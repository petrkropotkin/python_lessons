# Given a list of numbers, find and print all the list elements with an even index number.
# (i.e. A[0], A[2], A[4], ...).


# a)
a = [int(i) for i in input().split()]
for i in range(len(a)):
    if i%2 == 0:
        print(a[i],end = ' ')


# b)
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])