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

# property
"""Механизм, известный как свойства, обеспечивает  еще один способ определения методов,
вызываемых автоматически при обращении или присваивании атрибутам экземпляра. 
Свойства  –  это  тип  объектов,  который  присваивается  именам атрибутов  класса.
Они  создаются  вызовом  встроенной  функции  property,  которой  передаются  три  метода  
(обработчики  операций  чтения,  присваивания и удаления), и строкой документирования –
если в каком-либо аргументе передается значение None, следовательно, эта операция не поддерживается."""
# ---------------without property:--------------------------------
class classic:
    def __getattr__(self,name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

x = classic()
print(x.age) # Runs __getattr__ ==> 40
print(x.something) # Runs __getattr__ ==> AttributeError: something


# ---------- by using property:---------------------------------
class newprops:
    def getage(self):
        return 40
    age = property(getage, None, None,None) # get,set,del,docs

x = newprops()
print(x.age)  # Runs getage ==> 40
print(x.somethings) # AttributeError: 'newprops' object has no attribute 'somethings'

# ------------my example----------------------------------------
class P:
    def __init__(self, name):
        self.name = name

    @property
    def upper(self):
        return self.name.upper()

p = P('Vladimir')
print(p.upper) # VLADIMIR