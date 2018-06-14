"""
下面实现一个简单工厂模式

首先创建一个名为Animal的抽象产品，Animal是一个抽象基类，它带有方法do_say()，我们利用Animal接口创建来两种产品（cat和dog），并实现来do_say()方法来提供这些动物的叫声。ForestFactory是一个带有make_sount()方法的工厂，根据客户端传递的参数类型，它就可以在运行时创建适当的Animal实例，并输出正确的声音：
"""

from abc import ABCMeta, abstractmethod

# 抽象基类
class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

# 以下是两个产品
class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    def do_say(self):
        print("Meow Meow")

# forest facorry defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
