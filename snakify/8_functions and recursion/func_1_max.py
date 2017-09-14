
#============The built-in function max() in Python - like example============
# Everything passed to this function
# will gather the parameters into a single tuple called a,
# which is indicated by the asterisk.

def max(*a):
    maxi = a[0]
    for val in a[1:]:
        if val > maxi:
            maxi = val
    return maxi

print(max(3, 5, 4))