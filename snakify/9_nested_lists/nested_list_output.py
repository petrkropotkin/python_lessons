# =================output========================= :

# Nested loops

# a)
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):             # The first loop iterates through the row number,
    for j in range(len(a[i])):          # the second loop runs through the elements inside of a row.
        print(a[i][j], end=' ')
    print()
#=========================
print('2fth method:')
#=========================

# b)
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

#=========================
print('3fth method:')
#=========================

# c) by join()
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    print(' '.join([str(elem) for elem in row]))

#=========================
print('4fth method:')
#=========================
# d)

print('\n'.join([' '.join([str(i) for i in row]) for row in a]))