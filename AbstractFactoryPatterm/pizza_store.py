# 不知道怎么的就开了一家pizza店，用来生产一种pizza

class CheesePizza(object):           #第一种pizza
    def prepare(self):
        return "prepare Cheese pizza"
    def bake(self):
        return "bake Cheese pizza"
    def cut(self):
        return "cut Cheese pizza"
    def box(self):
        return "box Cheese pizza"
class GreekPizza(object):            #第二种pizza
    def prepare(self):
        return "prepare Greek pizza"
    def bake(self):
        return "bake Greek pizza"
    def cut(self):
        return "cut Greek pizza"
    def box(self):
        return "box Greek pizza"
class PepperoniPizza(object):        #第三种pizza
    def prepare(self):
        return "prepare Pepperoni pizza"
    def bake(self):
        return "bake Pepperoni pizza"
    def cut(self):
        return "cut Pepperoni pizza"
    def box(self):
        return "box Pepperoni pizza"



class SimplePizzaFactory(object):
# 定义一个createPizza方法，所有客户都使用这个方法来实例化新对象
    def createPizza(self, type):
    #===========这些跟之前的没有区别=============#
        self.type = type
        if self.type == "CHEESE":
            self.pizza = CheesePizza()
        if self.type == "GREEK":
            self.pizza = GreekPizza()
        if self.type == "PEPPERONI":
            self.pizza = PepperoniPizza()
    #返回一个pizza实例
        return self.pizza



class PizzaStore(object):
    def __init__(self):
        #将工厂传进来，委托工厂生产披萨实例
        self.factory = SimplePizzaFactory()
    #还是一样的orderPizza方法，只不过这次它不再自己生产了，而是通过工厂的createPizza方法，
    #传入需要的披萨种类，由工厂直接生产了
    def orderPizza(self, type):
        #通过工厂的createPizza方法，返回需要的披萨实例
        self.pizza = self.factory.createPizza(type)
        print(self.pizza.prepare())
        print(self.pizza.bake())
        print(self.pizza.cut())
        print(self.pizza.box())
