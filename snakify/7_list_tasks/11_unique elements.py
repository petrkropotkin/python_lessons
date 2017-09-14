# Given a list of numbers, find and print the elements that appear in the list only once.
# The elements must be printed in the order in which they occur in the original list.

# a)
a = [int(i) for i in input().split()]
a1 = []
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i], end = ' ')


# b)

a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')