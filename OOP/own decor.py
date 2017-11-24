class tracer:
    def __init__(self,func):
        self.calls = 0
        self.func = func
    def __call__(self,*args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer     #  spam = tracer(spam)
def spam(a,b,c):
    print (a, b, c)

spam(1, 2, 3)
print('==================================')
# ----  class decorator ----------------
def count(aClass):
    aClass.numInstances = 0
    return aClass
@count
class Spam:
    pass
@count
class Sup(Spam):
    pass


