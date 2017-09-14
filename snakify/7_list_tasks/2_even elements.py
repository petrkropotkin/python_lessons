# Given a list of numbers, find and print all elements that are an even number.
# In this case use a for-loop that iterates over the list,
#  and not over its indices! That is, don't use range()

a = [int(i) for i in input().split()]
for elem in a:
    if elem % 2 == 0:
        print(elem)