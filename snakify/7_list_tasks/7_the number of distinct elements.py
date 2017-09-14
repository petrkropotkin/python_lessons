# Given a list of numbers with all of its elements sorted in ascending order,
# determine and print the quantity of distinct elements in it.


# a)
a = [int(i) for i in input().split()]
a = set(a)
print(len(a))



# b)
a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)