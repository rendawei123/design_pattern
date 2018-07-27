"""
现实世界中的观察者模式
我们以新闻机构为例，新闻机构通常从不同地点收集新闻，并将其发布给订阅者

由于信息是实时发送或接收的，所以新闻机构应该尽快向其订户公布该消息。
此外，随着技术的进步，订户不仅可以订阅报纸，而且可以通过其他方式进行订阅，例如电子邮件、移动设备以及短信，
因此，我们还应该具备在将来添加任意其他订阅形式的能力，以便为未来的新技术做好准备
"""
from abc import ABCMeta, abstractclassmethod


class NewPublisher:
    """
    主题，提供了一个供订户使用的接口
    """
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        """
        提供观察者（Ob⬆️server）来注册NewsPublisherObserver
        """
        self.__subscribers.append(subscriber)

    def detach(self):
        """
        提供观察者来注销注册
        """
        return self.__subscribers.pop()

    def subscribers(self):
        """
        返回已经使用Subject注册的所有订户的类标
        """
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        """
        遍历已向NewsPublisher注册的所有订户的列表
        """
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        """
        创建新消息
        """
        self.__latestNews = news

    def get_news(self):
        """
        返回最新消息，并通知观察者
        """
        return "Got News:", self.__latestNews


class Subscriber(metaclass=ABCMeta):
    """
    观察者的抽象基类，具体观察者，用来实现观察者接口以保持其状态与主题中的变化一致
    """

    @abstractclassmethod
    def update(self):
        """
        有新闻发布的时候，他们就能得到Subject的相应通知
        """
        pass


class SMSSubscriber:
    """
    短信订阅
    """
    def __init__(self, publisher):
        """
        向NewPublisher进行注册
        """
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class EmailSubscriber:
    """
    邮件订阅
    """

    def __init__(self, publisher):
        """
        向NewPublisher进行注册
        """
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber:
    """
    其他订阅
    """

    def __init__(self, publisher):
        """
        向NewPublisher进行注册
        """
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


if __name__ == '__main__':
    # 客户端为NewPublisher创建一个对象，以供具体观察者用于各种操作
    news_publisher = NewPublisher()
    # 使用发布者的对象初始化短信、邮件、以及其他订阅方式的观察者类,其中__init__方法在内部使用attach方法进行注册以获取更新
    for subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscribers(news_publisher)

    # 打印已经通过主题注册的所有订户（具体观察者）
    print("\nSubscribers:", news_publisher.subscribers())
    # 创建新消息
    news_publisher.add_news("Hello World!")
    # 通知所有订户出现类新消息
    news_publisher.notify_subscribers()

    # 取消最后一个订阅
    print("\nDetached:", type(news_publisher.detach()).__name__)
    # 打印观察者
    print("\nSubscribers:", news_publisher.subscribers())

    # 创建第二条消息
    news_publisher.add_news("My second news!")
    # 通知所有订户出现类新消息
    news_publisher.notify_subscribers()