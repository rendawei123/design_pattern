"""
抽象工厂模式：
抽象工厂模式的目的是提供一个接口来创建一系列相关对象，而无需制定具体的类，工厂方法将创建实例的任务给类子类，而抽象工厂方法的目的是创建一系列相关对象

抽象工厂模式不仅仅确保客户端与对象的创建相互隔离，同时还确保客户端能够使用创建的对象。但是，客户端只能通过接口访问对象，如果要使用一个系列中的多个产品，那么抽象工厂模式能够帮助客户端一次使用来自一个产品/系列的多个对象

如果我们正在开发的应用应该是平台无关的，则它需要对各种依赖项进行抽象处理，这些依赖项包括操作系统、文件系统调用，等等。抽象工厂模式负责为整个平台创建所需的服务，这样的话，客户端就不必直接创建平台对象了。

例子：
"""

# 现在我们开办了一家披萨店，供应美味的印式披萨和美式披萨。为此，我们首先创建一个抽象基类
from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def createVegPizza(self):
        """
        蔬菜披萨
        """
        pass

    @abstractmethod
    def createNonVegPizza(self):
        """
        非蔬菜披萨
        """
        pass

class IndianPizzaFactory(PizzaFactory):
    """
    印式披萨
    """
    def createVegPizza(self):
        return DeluxVeggiePizza()  # 豪华素食披萨

    def createNonVegPizza(self):
        return ChickenPizza()  # 鸡肉披萨


class USPizzaFactory(PizzaFactory):
    """
    美式披萨
    """
    def createVegPizza(self):
        return MexicanVegPizza()  # 墨西哥蔬菜披萨

    def createNonVegPizza(self):
        return HamPizza()  # 火腿披萨


"""
下面我们来定义VegPizza和NonPizza，他们定义了自己的方法，分别是prepart()和server(),
这里的想法是，素食披萨有适当的外皮、蔬菜和调味料，非素食披萨在素食披萨上搭配非素食食材。

就本例而言，我们将创建DeluxVeggiePizza和MexicanVegPizza，并实现prepare方法，
接下来定义ChickenPizza和HamPizza,并实现server()方法
"""

class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass

class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def server(self, VegPizza):
        pass

class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)

class ChickenPizza(NonVegPizza):
    def server(self, VegPizza):
        print(type(self).__name__, "is served with Chicken on ", type(VegPizza).__name__)

class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):
    def server(self, VegPizza):
        print(type(self).__name__, "is served with Chicken on ", type(VegPizza).__name__)


"""
最终，当用户来到PizzaStore并要一份美式非素食pizza的时候，USPizzaFactory负责准备素食，然后在上面加上火腿，马上就编程非素食披萨了
"""

class PizzaStore:
    def __init__(self):
        pass
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.server(self.VegPizza)

if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.makePizzas()
