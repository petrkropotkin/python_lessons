# given: s = 'ab12c59p7dq'
# you need to extract digits from the list s
# to make it so:
# digits == [1, 2, 5, 9, 7]
s = 'ab12c59p7dq'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)

# ==========......Split and join methods.....====================
# the input is a string
# 1 2 3
s = input() # s == '1 2 3'
a = s.split() # a == ['1', '2', '3']
print(a)

# If you want to get the list of numbers,
#  you have to convert the list items one by one to integers:

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(a) # [1, 2, 3]

# Using the special magic of Python — generators —
#  the same can be done in one line:
a = [int(s) for s in input().split()]
print(a) # [1, 2, 3]


a = ['red', 'green', 'blue']
print(' '.join(a))
# return red green blue

a = [1, 2, 3]
print(' '.join([str(i) for i in a]))
# the next line causes a type error,
# as join() can only concatenate strs
# print(' '.join(a))