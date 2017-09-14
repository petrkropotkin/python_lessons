# A cupcake costs A dollars and B cents. Determine, how many dollars
# and cents should one pay for N cupcakes.
# A program gets three numbers: A, B, N. It should
# print two numbers: total cost in dollars and cents.
a = int(input())
b = int(input())
n = int(input())
cost_n = n*(a*100+b)
print(cost_n//100,cost_n%100)