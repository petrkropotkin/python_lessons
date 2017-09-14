# Given an integer not less than 2. Print its smallest integer divisor greater than 1
# 15==> 3
#------------my solution:-------------------

n = int(input())
i = n
while i > 1:
    if n%i == 0:
        smallest_div = i
    i -= 1
else:
    print(smallest_div)


#------------Suggested solution-----------

n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
