"""
通常程序员需要的是让实例共享相同的状态，开发人员应该关注状态和行为，而不是同一性，（单例模式是同一性）由于该概念基于所有对象共享相同的状态，因此它也被称为Monostate(单态)模式。

这种模式和单例模式不同的一点是，单例模式是相同的对象，不同的状态，单态模式是不同的对象，相同的状态
"""

# class Borg:
#     __shared_state = {"1":"2"}
#     def __init__(self):
#         self.x = 1
#         self.__dict__ = self.__shared_state
#         pass
#
# b = Borg()
# b1 = Borg()
# b.x = 4
#
# print(b)
# print(b1)
# print(b.__dict__)
# print(b1.__dict__)

# 从打印结果可以看到，实例化出了不同的类，但是有相同的状态

# <__main__.Borg object at 0x1039072e8>
# <__main__.Borg object at 0x103907358>
# {'1': '2', 'x': 4}
# {'1': '2', 'x': 4}

"""
除此之外，我们还可以通过修改__new__方法本身来实现Borg模式。我们知道，__new__方法是用来创造对象的实例的
"""

class Borg(object):
    __shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj
