# Statement
# The virus attacked the filesystem of the supercomputer and broke the control of access rights to the files.
# For each file there is a known set of operations which may be applied to it:
#
# write W,
# read R,
# execute X.
#
# The first line contains the number N — the number of files contained in the filesystem.
# The following N lines contain the file names and allowed operations with them, separated
# by spaces. The next line contains an integer M — the number of operations to the files.
# In the last M lines specify the operations that are requested for files. One file can be requested many times.
# You need to recover the control over the access rights to the files.
# For each request your program should return OK
# if the requested operation is valid or Access denied if the operation is invalid.
# input
"""
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog     # --- operations ==> files----
"""

# output
# OK
# Access denied
# Access denied
# OK
# OK

list_file = []
dic_file_0 = {}
set_operations = {'write': 'W', 'read': 'R', 'execute': 'X'}
for i in range(int(input())):
    a = input().split()
    list_file.append(a)
# [['helloworld.exe', 'R', 'X'], ['pinglog', 'W', 'R'], ['nya', 'R'], ['goodluck', 'X', 'W', 'R']]

for i in list_file:
    dic_file_0[i[0]] = list(i[1:])

# {'helloworld.exe': ['R', 'X'], 'pinglog': ['W', 'R'], 'nya': ['R'], 'goodluck': ['X', 'W', 'R']}

for i in range(int(input())):
    a,b = input().split()

    if set_operations[a] in dic_file_0[b]:
            print("OK")
    else:
        print("Access denied")



#=========Suggested solution==============

OPERATION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions) #  very interesting use of the set !!!

for i in range(int(input())):
    operation, file = input().split()
    if OPERATION_PERMISSION[operation] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')












