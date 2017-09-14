# A sequence consists of integer numbers and ends with the number 0. Determine the index
# of the largest element of the sequence.
# If the highest element is not unique, print the index of the first of them.

#-----------------------------my solution-----------------------------------

n = int(input())
largest = n
index = 1
largest_index = 1

while n != 0:
    n = int(input())
    index += 1
    if n > largest:
        largest = n
        largest_index = index

print(largest_index)

# --------------------------Suggested solution----------------------------------

max = 0
index_of_max = -1
element = -1
len = 1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)

