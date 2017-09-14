# The Fibonacci sequence is defined as follows:
# ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
# ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
# Given a non-negative integer nn, print the nnth Fibonacci number ϕn.
# This problem can also be solved with a for loop
# index ==> Fibonacci number; 6==> 8


# --------------------------my solution------------------------
n = int(input())
x = 0
y = 1
с = 0
while с < n:
    x, y = y, x + y
    с += 1
print(x)

# -----------------Suggested solution---------------------------
# n = int(input())
# if n == 0:
#     print(0)
# else:
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     print(b)

# ===================from net======================================
# http://younglinux.info/algorithm/fibonacci
# def fib(n):
#     a = 0
#     b = 1
#     for __ in range(n):
#         a, b = b, a + b
#     return a
# print(fib(2))

# =========================================================================
# =========================================================================
# Числа Фибоначчи – это ряд чисел,
# в котором каждое последующее число равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13 и т.д.
#
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
# ========================================================================