# Given a list of numbers, find and print all the elements that are greater than the previous element.

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])