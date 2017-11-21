from employees import PizzaRobot, Server
"""Now that we’ve implemented our employees, let’s put them in the pizza shop and let
them get busy. Our pizza shop is a composite object: it has an oven, and it has employees
like servers and chefs. When a customer enters and places an order, the components
of the shop spring into action—the server takes the order, the chef makes the pizza,
and so on. """


class Customer:
    def __init__(self,name):
        self.name = name

    def order(self,server):
        print(self.name, 'orders from',server)

    def pay(self,server):
        print(self.name,'pays for item to', server)

class Oven:
    def bake(self):
        print('oven bakes')

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')    # Embed other objects
        self.chef = PizzaRobot('Bob')  # A robot named bob
        self.oven = Oven()

    def order(self,name):
        customer = Customer(name)     # Activate other objects
        customer.order(self.server)   # Customer orders from server
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    scene = PizzaShop()     # Make the composite
    scene.order('Homer')    # Simulate Homer's order
    print('...')
    scene.order('Shaggy')   # Simulate Shaggy's order


# Homer orders from <Employee: name=Pat, salary=40000>
# Bob makes pizza
# oven bakes
# Homer pays for item to <Employee: name=Pat, salary=40000>
# ...
# Shaggy orders from <Employee: name=Pat, salary=40000>
# Bob makes pizza
# oven bakes
# Shaggy pays for item to <Employee: name=Pat, salary=40000>


