L1 = [1]*10
L2 = list(range(1,10))
for (x,y) in zip(L1,L2):
    print('{0} + {1} = '.format(x, y), x + y)

print('-----------------------------------')
name = ('Vova','Vasya','Inokentiy')
age = (33,35,15)
my_dict = dict(zip(name,age))
print(my_dict)


# 1 + 1 =  2
# 1 + 2 =  3
# 1 + 3 =  4
# 1 + 4 =  5
# 1 + 6 =  7
# 1 + 7 =  8
# 1 + 8 =  9
# 1 + 9 =  10
# -----------------------------------
# {'Vova': 33, 'Vasya': 35, 'Inokentiy': 15}
