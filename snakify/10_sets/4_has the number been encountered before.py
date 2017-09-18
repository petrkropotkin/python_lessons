# Given a sequence of numbers, determine if the next number has already been encountered. For each number,
# print the word YES (in a separate line) if this number has already been encountered, and print NO,
# if it has not already been encountered.
a = input().split()
storage = set()
for i in a:
    if i in storage:
        print('YES')
    else:
        print('NO')
        storage.add(i)
