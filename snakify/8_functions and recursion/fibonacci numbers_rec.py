# Given a non-negative integer nn, print the nnth Fibonacci number.
# Do this by writing a function fib(n) which takes the non-negative integer
# nn and returns the nnth Fibonacci number.
# Don't use loops, use the flair of recursion instead.'
#    ' However, you should think about why the recursive method is much slower than using loops.

# index ==> Fibonacci number; 6==> 8
# Формула:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2
# Пример вычисления:
# F3 = F2 + F1 = 1 + 1 = 2
# F4 = F3 + F2 = 2 + 1 = 3
# F5 = F4 + F3 = 3 + 2 = 5
# F6 = F5 + F4 = 5 + 3 = 8


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(2))