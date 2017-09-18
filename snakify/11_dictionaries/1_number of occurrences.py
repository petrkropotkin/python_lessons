# The text is given in a single line.
# For each word of the text count the number of its occurrences before it.
# A word is a sequence of non-whitespace characters. Two consecutive words
# are separated by one or more spaces. Punctiation marks are a part of a word, by this definition.
# input
# one two one tho three
# output
# 0 0 1 0 0

text = input().split()
my_dic = {}

for word in text:
    if word not in my_dic:
        my_dic[word] = 0
        print(my_dic[word],end = ' ')
    else:
        my_dic[word] += 1
        print(my_dic[word],end = ' ')

# ================Suggested solution=================
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
