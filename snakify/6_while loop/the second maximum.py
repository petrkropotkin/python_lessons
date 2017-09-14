# The sequence consists of distinct positive integer numbers and ends with the number 0.
# Determine the value of the second largest element in this sequence.
# It is guaranteed that the sequence has at least two elements.

maxi_first = int(input())
maxi_second = int(input())
n = int(input())

if maxi_first < maxi_second:
    maxi_first, maxi_second = maxi_second, maxi_first

while n != 0:
    if maxi_first < n:
        maxi_second, maxi_first = maxi_first, n

    elif maxi_second < n:
        maxi_second = n

    n = int(input())
print(maxi_second)

#=============for list==========================================

a = [2,1,4,3,5]
maxi_first = a[0]
maxi_second = a[1]

if maxi_first < maxi_second:
    maxi_first, maxi_second = maxi_second, maxi_first

for i in range(len(a)):
    if maxi_first < a[i]:
        maxi_second, maxi_first = maxi_first, a[i]

    elif maxi_second < a[i]:
            maxi_second = a[i]


print(maxi_second)
