# Determine the number of even elements in the sequence ending with the number 0
#============my solution===========================

n = int(input())
counter = 0

while n != 0:
    if n % 2 == 0:
        counter += 1

    n = int(input())

print(counter)

#==============Suggested solution===================

num_even = -1
element = -1
while element != 0:
    element = int(input())
    if element % 2 == 0:
        num_even += 1
print(num_even)