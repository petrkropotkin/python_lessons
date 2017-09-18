# Given the text: the first line contains the number of lines, then given the lines of words.
# Print the word in the text that occurs most often. If there are many such words,
# print the one that is less in the alphabetical order.
# input
"""
1
apple orange banana banana orange
"""
# output
# banana

my_dic = {}
for i in range(int(input())):
    for j in input().split():
        my_dic[j] = my_dic.get(j,0) + 1

maxi_val = max(my_dic.values())

list_temp = []
for key,val in my_dic.items():
    if val == maxi_val:
        list_temp.append(key)

print(min(list_temp))

# =====Suggested solution==========

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count] #creasy solution :)
print(min(most_frequent))
