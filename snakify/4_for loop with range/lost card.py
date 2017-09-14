# There was a set of cards with numbers from 1 to N.
# One of the card is now lost. Determine the number
# on that lost card given the numbers for the remaining cards.
# Given a number N, followed by N − 1 integers - representing
# the numbers on the remaining cards (distinct integers in the
# range from 1 to N). Find and print the number on the lost card.

N = int(input())
prog =((N+1)*N)//2
summa = 0
for i in range(1,N):
    number = int(input())
    summa += number
print(prog-summa)
