"""
以一个计算机系统为例

计算机可以有多个状态，如开机、关机、挂起、休眠
"""


class ComputerState:
    """
    计算机状态
    """
    name = "state"  # 对象的状态
    allowed = []  # 定义允许进入状态的对象的列表

    def switch(self, state):
        """
        用来实际改变对象的状态
        """
        if state.name in self.allowed:  # 如果此状态允许
            print('Current:', self, ' => switching to', state.name)
            self.__class__ = state  # 切换状态

        else:
            print("Current:", self, ' => switching to', state.name, 'not possible.')

    def __str__(self):
        """
        定义类的名称
        """
        return self.name


"""
下面定义4个计算机状态
"""


class Off(ComputerState):
    """
    这将关闭计算机，这时候允许的状态只有on
    """
    name = "off"
    allowed = ['on']


class On(ComputerState):
    """
    这将打开计算机。这时候允许的状态是off， suspend（挂起）和hibernate（休眠）
    """
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    """
    挂起，当计算即处于这种状态时，只能执行打开操作
    """
    name = "suspend"
    allowed = ['on']


class Hibernate(ComputerState):
    """
    休眠，当计算机处于这种状态时，只能执行打开操作
    """
    name = "hibernate"
    allowed = ['on']


class Computer:
    """
    context类，用于执行状态的切换
    """
    def __init__(self, model='HP'):
        """
        定义计算机的基本状态
        """
        self.model = model
        self.state = Off()

    def change(self, state):
        """
        更改对象的状态，但是行为的实际更改是由前面的几个类来实现的, 注意，这个state直接用类，不用实例化
        """
        self.state.switch(state)


if __name__ == '__main__':
    comp = Computer()
    comp.change(On)
    comp.change(On)
