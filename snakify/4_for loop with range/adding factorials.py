# Given an integer nn, print the sum 1!+2!+3!+...+n!1!+2!+3!+...+n!.

n = int(input())
fact = 1
summa_fact = 0
for i in range(1, n + 1):
    fact *= i
    summa_fact += fact

print(summa_fact)