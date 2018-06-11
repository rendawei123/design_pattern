"""
单例模式提供了这样一个机制，即确保有且只有一个特定类型的对象，并提供全局访问点
"""

# 经典的单例模式
# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance

# s = Singleton()
# print(s)
# s1 = Singleton()
# print(s1)

"""
单例模式的用例之一就是懒汉式实例化，例如，在导入模块的时候，我们可能会无意间创建一个对象，但当时根本用不到它。懒汉式实例化能确保在实际需要时才创建对象，它是一种节约资源并仅仅在需要时才创建他们的方式。
"""
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print('__init__method called..')
        else:
            print('Instance already created', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()  # 只是初始化了，但是不是单例
s1 = Singleton.getInstance()
s2 = Singleton.getInstance()
s4 = Singleton()  # 只是初始化了，但是不是单例
print(s)
print(s1)
print(s2)
print(s4)
