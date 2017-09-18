# As you know, the president of USA is elected not by direct vote,
# but through a two-step voting. First elections are held in each state and determine
# the winner of elections in that state.
# Thereafter, the state election is going: in this election, every state has a
# certain the number of votes — the number of electors from that state.
# In practice, all the electors from the state of voted in accordance with the results of the vote within a state.
# The first line contains the number of records. After that, each entry
# contains the name of the candidate and the number of votes they got in one of the states.
# Count the total results of the elections: sum the number of votes for each candidate.
#     Print candidates in the alphabetical order.
# input
"""
5
McCain 10
McCain 5
Obama 9
Obama 8
McCain 1  """

# output
# McCain 16
# Obama 17

my_dic = {}

for i in range(int(input())):
    a,b = input().split()
    if a not in my_dic:
        my_dic[a] = int(b)
    else:
        my_dic[a] += int(b)

# print(my_dic)

for j in sorted(my_dic.keys()):
    print (j, my_dic[j])

#===========suggested solution===================
#
num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes) # very interesting solution !!!

for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)
