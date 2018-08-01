"""
我们以一个简单的按钮来实现电视机遥控器，执行开/关动作。如果电视打开，这个遥控器按钮将关闭电视，反之亦然
"""

from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    """
    定义相应的方法来执行开/关操作
    """
    @abstractmethod
    def do_this(self):
        pass


class StartState(State):
    """
    执行开操作
    """
    def do_this(self):
        print("TV Switching ON..")


class StopState(State):
    """
    执行关操作
    """
    def do_this(self):
        print("TV Switching OFF..")


class TVContext(State):
    """
    实现State接口并维护当前状态的引用
    """
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def do_this(self):
        self.state.do_this()


if __name__ == '__main__':
    context = TVContext()
    context.get_state()

    start = StartState()
    stop = StopState()
    context.set_state(stop)
    context.do_this()