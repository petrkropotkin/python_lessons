# A sequence consists of integer numbers and ends with the number 0.
# Determine how many elements of this sequence are equal to its largest element.
# 1 3 3 0 ==> 2

n = int(input())
maxi = n
counter_maxi = 0

while n != 0:

    if n > maxi:
        maxi = n
        counter_maxi = 1

    elif n == maxi:
        counter_maxi += 1
    n = int(input())

print(counter_maxi)
