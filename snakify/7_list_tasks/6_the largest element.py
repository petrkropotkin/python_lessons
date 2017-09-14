# Given a list of numbers. Determine the element in the list with the largest value.
# Print the value of the largest element and then the index number.
# If the highest element is not unique, print the index of the first instance.

# a)========================================

a = [int(i) for i in input().split()]
largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
print(largest,a.index(largest))

# b)========================================

index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)

