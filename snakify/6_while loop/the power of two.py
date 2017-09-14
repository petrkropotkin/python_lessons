# For a given integer N, find the greatest integer x where 2**x is less than
# or equal to N. Print the exponent value and the result of the expression 2**x.
# 50==> 5  32
# ----------my solution-----------------------

n = int(input())
x = 1
res = 1
while 2**x <= n:
    res = 2**x
    x += 1
print(x-1,res)

# --------Suggested solution------------------

n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)