"""
以下是完整的命令模式
"""

from abc import ABCMeta, abstractclassmethod


class Command(metaclass=ABCMeta):
    """
    声明执行操作的接口
    """
    def __init__(self, recv):
        self.recv = recv

    @abstractclassmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    """
    将一个Receive对象和一个操作绑定在一起
    """
    def execute(self):
        self.recv.action()


class Receiver:
    """
    知道如何实施与执行一个请求相关操作
    """
    def action(self):
        print('Receive Action')


class Invoker:
    """
    调用者,知道如何实施与执行一个请求相关操作
    """
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == '__main__':
    # 接收命令
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    # 执行命令
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
