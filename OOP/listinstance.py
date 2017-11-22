# Listing instance attributes with __dict__
class ListInstance:
    """
       Mix-in class that provides a formatted print() or str() of instances via
       inheritance of __str__ coded here;  displays instance attrs only;  self is
       instance of lowest class; __X names avoid clashing with client's attrs
       """
    def __str__(self):
        return '<Instance of %s, address %s: \n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )

    def __attrnames(self):
        result = ''
        for attr in sorted (self.__dict__):
            result += '\tname %s = %s\n' % (attr, self.__dict__[attr])
        return result

if __name__ == '__main__':
   class ForTest(ListInstance):
       def __init__(self,data):
           self.data = data


   x = ForTest (45)
   print(x)





