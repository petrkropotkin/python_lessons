# immutable data type can be an element of a set: a number, a string, a tuple.
# mutable (changeable) data types cannot be elements of the set(list,another set)
# A = {1, 2, 3}
#
# print(1 in A, 4 not in A)
# A.add(4)# set.add adds an individual element to the set
#
# B = set()
# B.update(A)
# print(B)
l = [4,56]

s = set()
d = s.update(l)# you can pass multiple iterables to it and it will iterate all iterables
print(d) #==>  {56, 4}
# s.update(4)# ==> TypeError: 'int' object is not iterable

