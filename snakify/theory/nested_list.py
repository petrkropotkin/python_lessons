for i in range(4):
    for j in range(4):
        print(1, end='')
    print()



n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):  #---увеличиваем i на каждом шаге!!!
        print(j, sep='', end='')
    print()

print()

for i in range(5,-1,-1):
    for j in range(i+1):
        print(1,end='')
    print()

#----------------------------------------------------------
print()
#==========================================================
array = []
for i in range(0, 4):
    temp = []
    for j in range(0, 4):
        temp.append(1)
    array.append(temp)
#----------------------
print(array)


#----------------------------------------------------------
print()
#==========================================================

array = []
for i in range(8):
    temp = []
    for j in range(8):
        if j % 2 == 0:
            temp.append('white')
        else:
            temp.append('black')
    if i % 2 != 0:
        temp.reverse()
    array.append(temp)

for i in array:
    print(i)
