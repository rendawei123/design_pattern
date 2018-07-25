"""
让我们通过一个简单的例子来理解该模式
以演员与他的经纪人为例，当制作公司在拍电影时，他们通常会与经纪人交流，而不是直接跟演员交流。
经纪人会根据演员的日程安排和其他合约情况来答复制作公司该演员是否有空。
下面的代码中，Actor是代理，对象Agent用于查看Actor是否处于忙碌状态。
如果Actor正忙，调用Actor().occupied()方法，如果不忙，则返回Actor().avaliable()方法。
"""


class Actor(object):
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied with current movie")

    def avaliable(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie")

    def getStatus(self):
        return self.isBusy


class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.avaliable()


"""
代理模式主要完成了一下工作
它为其他对象提供了一个代理，从而实现了对原始对象的访问控制
它可以用作一层或接口，以支持分布式访问
它通过增加代理，保护真正的组建不受意外的影响。
"""

"""
下面以
"""
if __name__ == '__main__':
    r = Agent()
    r.work()
