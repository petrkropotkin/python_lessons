# static method
# first way
""" Функции, которым не передаются ссылки на экземпляры,
в Python 3 могут вызываться обычным образом через имя класса,
но в Python 2 по умолчанию – никогда."""
class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances(): # static method without self
        print("Number of instances created: ",Spam.numInstances)

a = Spam()
b = Spam()
Spam.printNumInstances()
# a.printNumInstances() # TypeError: printNumInstances() takes 0 positional arguments but 1 was given
print('==================================')
# second way
class Spam_2:
    numInstances = 0
    def __init__(self):
        Spam_2.numInstances += 1
    def printNumInstances():
        print ("Number of instances created: ", Spam_2.numInstances)

    printNumInstances = staticmethod(printNumInstances)

a = Spam_2()
b = Spam_2()
Spam_2.printNumInstances() # Number of instances created:  2
b.printNumInstances() # Number of instances created:  2
print('==================================')
# third way ==> Class Method
class Spam_3:
    numInstances = 0    # Use class method instead of static
    def __init__(self):
        Spam_3.numInstances += 1
    def printNumInstances(cls):
        print('Number of instances:', cls.numInstances)
    printNumInstances = classmethod(printNumInstances)

a, b = Spam_3(), Spam_3()
a.printNumInstances()       # Passes class to first argument
Spam_3.printNumInstances()    # Also passes class to first argument
