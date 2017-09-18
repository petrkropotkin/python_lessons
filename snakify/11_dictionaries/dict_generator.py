#input
"""
3
Ukraine Kiev
Russia Moscow
USA Washington   """

n = int(input())
my_dic = dict([[j for j in input().split()] for i in range(n)])
print(my_dic)