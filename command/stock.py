"""
我们通过一个证券交易所的例子来演示命令模式

作为用户，你会创建买入或卖出股票的订单，通常情况下，你无法直接执行买入或卖出
实际上，代理或经纪人在你和证券交易所之间扮演来中介的角色
代理负责将你的请求提交给证券交易所，假设你想再星期一早上开市后卖出股票
但是在星期日晚上，虽然交易所尚未开市，你就可以向代理提出卖出股票的请求，
然后，代理会将该请求放入排队，以便在星期一早晨当交易所开市的时候执行该请求，完成交易
"""
from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    """
    提供抽象类，Command对象,提供一个接口，以便ConcreteCommand可以实现该行为
    """

    @abstractmethod
    def execute(self):
        """
        定义抽象方法
        """
        pass


class BuyStockOrder(Order):
    """
    实现Order接口，可以为交易系统定义适当的操作, 购买命令
    """
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    """
    卖出股票命令
    """
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    """
    股票交易系统，也就是命令模式中的Receiver对象
    """
    def buy(self):
        """
        购买股票
        """
        print("You will buy stocks")

    def sell(self):
        """
        卖出股票
        """
        print("You will sell stocks")


class Agent:
    """
    调用者,也就是代理，是客户端和交易所之间的中介，并执行客户下达的订单
    """
    def __init__(self):
        """
        客户端下达的任何新订单都将添加到队列中
        """
        self.order_queue = []

    def place_order(self, order):
        """
        负责对订单排序以及执行订单
        """
        self.order_queue.append(order)
        order.execute()


if __name__ == '__main__':
    # 客户端首先设置其接收者
    stock = StockTrade()
    # 创建订单命令
    buy_stock = BuyStockOrder(stock)
    sell_stock = SellStockOrder(stock)

    # 创建调用者
    agent = Agent()
    agent.place_order(buy_stock)
    agent.place_order(sell_stock)
