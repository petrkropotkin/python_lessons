
# ==========[expression for variable in sequence]============

n = 5
a = [i ** 2 for i in range(n)]
print(a)

# ===========================================================

from random import randrange
n = 10
a = [randrange(1, 10) for i in range(n)]
print(a)

# ===========================================================

# And in this example the list will consist of lines read from standard input:
# first, you need to enter the number of elements of the list
# (this value will be used as an argument of the function range),
#  second — that number of strings:

a = [input() for i in range(int(input()))]
print(a)
