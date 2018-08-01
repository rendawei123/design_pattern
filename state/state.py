"""
理解state状态设计模式
"""

from abc import abstractmethod, ABCMeta


class State(metaclass=ABCMeta):
    """
    封装对象行为的接口，这个行为与对象的状态相关联
    """
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateB(State):
    """
    实现State接口的子类
    """
    def handle(self):
        print("ConcreteStateB")


class ConcreteStateA(State):
    """
    实现State接口的子类
    """
    def handle(self):
        print("ConcreteStateA")


class Context(State):
    """
    定义了用户感应区的接口
    """
    def __init__(self):
        self.state = None

    def get_state(self):
        """
        获取状态
        """
        return self.state

    def set_state(self, state):
        """
        设置状态, 维护了一个ConcreteState子类的实例，该子类在内部定义了对象的特定状态的实现
        """
        self.state = state

    def handle(self):
        self.state.handle()


if __name__ == '__main__':
    context = Context()
    stateA = ConcreteStateA()
    stateB = ConcreteStateB()

    context.set_state(stateA)
    context.handle()
