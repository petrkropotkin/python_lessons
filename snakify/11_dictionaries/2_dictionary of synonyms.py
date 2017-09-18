# You are given a dictionary consisting of word pairs. Every word is a synonym
# the other word in its pair. All the words in the dictionary are different.
# After the dictionary there's one more word given. Find a synonym for him.
# input
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye

# output
# Bye
# решение -  в словарь сначало первое слово является ключом, а затем наоборот




my_dic = {}
for i in range(int(input())):
    a,b = input().split()
    my_dic[a] = b
    my_dic[b] = a
synonym = input()

print(my_dic[synonym])

#-------------second variant----------------------------

my_dic = dict([[j for j in input().split()] for i in range(int(input()) )])
synonym = input()
for key in my_dic:
    if synonym == key:
        print(my_dic[key])
    else:
        if synonym == my_dic[key]:
            print(key)


#===================third variant=======================
n = int(input())
p = dict(input().split() for j in range(n))
k = input()
for key, value in p.items():
    if k == value:
        print(key)
    if k == key:
        print(value)









