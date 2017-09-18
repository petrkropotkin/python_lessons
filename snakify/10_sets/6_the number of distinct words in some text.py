# Given a number n, followed by nn lines of text,
# print the number of distinct words that appear in the text.
# For this, we define a word to be a sequence of non-whitespace characters,
# seperated by one or more whitespace or newline characters.
# Punctuation marks are part of a word, in this definition.

# input
# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.

# output
# 19

a = []
for i in range(int(input())):
    a.append(input().split())

s = set()
for row in a:
    for elem in row:
        s.add(elem)
print(len(s))

#===========Suggested solution======================
words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))