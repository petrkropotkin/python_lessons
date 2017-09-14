# Given the three integers, print the least of them.
a = int(input())
b = int(input())
c = int(input())

mini_3 = a

if mini_3 > b :
    mini_3 = b
if mini_3 > c:
    mini_3 = c

print(mini_3)


