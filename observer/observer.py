"""
观察者设计模式的具体实现
"""


class Subject:
    """
    主题类
    """
    def __init__(self):
        self.__observers = []

    def resister(self, observer):
        """
        observer（观察者）通过此方法注册到主题类中
        """
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    """
    观察者1
    """
    def __init__(self, subject):
        subject.resister(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ": Got", args, "From", subject)


class Observer2:
    """
    观察者2
    """
    def __init__(self, subject):
        subject.resister(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ": Got", args, "From", subject)

if __name__ == '__main__':
    subject = Subject()
    observer1 = Observer1(subject)
    observer2 = Observer2(subject)
    subject.notify_all("notification")
