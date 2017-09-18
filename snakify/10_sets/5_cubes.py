# Alice and Bob like to play with colored cubes.
# Each child has its own set of cubes and each cube has a distinct color,
# but they want to know how many unique colors exist if they combine their block sets.
# To determine this, the kids enumerated each distinct color with a random number from
# 0 to 10**8. At this point their enthusiasm dried up, and you are invited to help them finish the task.
# Given two integers that indicate the number of blocks in Alice's and then Bob's sets N and M.
# The following N lines contain the numerical color value for each cube in Alice's set.
# Then the last M rows contain the numberical color value for each cube in Bob's set.
#
# Find three sets: the numerical colors of cubes in both sets, the numerical colors of
# cubes only in Alice's set, and the numerical colors of cubes only in Bob's set.
# For each set, print the number of elements in the set, followed by the numerical
# color elements, sorted in ascending order.

n, m = [int(i) for i in input().split()]

alice_set = set()
for i in range(n):
    alice_set.add(int(input()))

bob_set = set()
for i in range(m):
    bob_set.add(int(input()))


first_set = alice_set&bob_set
second_set = alice_set - bob_set
third_set = bob_set - alice_set


for i in first_set, second_set, third_set:
    print(len(i))
    print(*sorted(i))

#================Suggested solution=============================
def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])


N, M = [int(s) for s in input().split()]
A_colors, B_colors = set(), set()
for i in range(N):
    A_colors.add(int(input()))
for i in range(M):
    B_colors.add(int(input()))

print_set(A_colors & B_colors)
print_set(A_colors - B_colors)
print_set(B_colors - A_colors)