"""
元类
元类是一个类的类
类的定义由它的元类决定，所以当我们用类A创建一个类时，python通过A=type(name,bases,dict)创建它。
name：类的名称
bases：基类
dict：属性变量
"""

# 现在，如果一个类有一个预定义的元类（名为Metals），那么python就会通过A=Metals(name,bases,dict)来创建类。

# 以下例子为示例元类的实现
# 元类
# class MyInt(type):
#     def __call__(cls, *args, **kwargs):
#         print('******** Here is My int ******', args)
#         print("Haw do whatever you want with these objects...")
#         return type.__call__(cls, *args, **kwargs)
#
# # 类
# class int(metaclass=MyInt):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# i = int(4, 5)
"""
对于已经存在的类来说，当需要创建对象时， 将调用python的特殊方法__call__
"""
# 以下是基于元类实现的单例模式

class MetaSingleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
