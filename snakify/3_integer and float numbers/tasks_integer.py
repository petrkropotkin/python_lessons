# Given an integer number, print its last digit.
# n = int(input())
# print(n%10)

# Given a positive real number, print its fractional part.
# n = float(input())
# print(n%int(n))

# Given a positive real number,
#  print its first digit to the right of the decimal point.
# n = float(input())
# print(int((n-int(n))*10))
# #or
# print(int(n * 10) % 10)

# A car can cover distance of N kilometers per day.
# How many days will it take to cover a route of length M kilometers?
# The program gets two numbers: N and M.
# N = int(input())
# M = int(input())
# from math import ceil
# print(ceil(M/N))


# Given an integer. Print its tens digit. 1234==> 3
# n = int(input())
# print(n%100//10)


# Given a three-digit number. Find the sum of its digits.
n = int(input())
print(n//100+n//10%10+n%10)

