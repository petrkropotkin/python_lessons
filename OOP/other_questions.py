class UsingSlots:
    __slots__ =['a', 'b']


x = UsingSlots()
x.a = 25
print(x.a) # 25
print(getattr(x,'a'))  # 25
setattr(x,'b',27)
print(x.b)  # 27

# x.c = 40
# print(x.c)  #AttributeError: 'UsingSlots' object has no attribute 'c'
# print(x.__dict__)   # AttributeError: 'UsingSlots' object has no attribute '__dict__'

