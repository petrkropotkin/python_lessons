# create
Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}

Capitals = dict(RA = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')

Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])

Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))

print(Capitals)



# getting value of the element by its key
print(Capitals["USA"])  #==> Washington
print(Capitals.get('Ukraine', "there is'nt"))  # ==>Kiev
print(Capitals.get('Moldova', "there is'nt"))  # ==> there is'nt
print(Capitals.get('Moldova'))  # ==> None

# add a new item to the dictionary
Capitals['Moldova'] = 'Chișinău'
print(Capitals)

# remove an item from the dictionary
del Capitals["Russia"] # operation raises an exception KeyError if there is no such key in the dictionary.

# two safe ways to remove an item from the dictionary
# -------------------1---------------------
A = {'ab' : 'ba', 'aa' : 'aa', 'bb' : 'bb', 'ba' : 'ab'}

key = 'ac'
if key in A:
    del A[key]

# -------------------2----------------------
try:
    del A[key]
except KeyError:
    print('There is no element with key "' + key + '" in dict')
print(A)

# ---------remove an item from the dictionary by the method pop-----------
# =============A.pop(key)=================
print(A.pop('ba'))#  ==> ab
#print(A.pop('zzz')) # ==> KeyError: 'zzz'

# -------------A.pop(key, None)-----------
print(A.pop('zzz','there is not'))#==> 'there is not'



# Iterating dictionary
# ------------------1---------------------
A = dict(zip('abcdef', list(range(6))))

for key in A:

    print(key, A[key])

# ------------------2---------------------
A = dict(zip('ghiklm', list(range(6))))
for key, val in A.items():
    print(key, val)