"""
现在通过一个数据库应用程序来展示单例的应用，操作数据库就要对数据库进行多种读取和写入，完整的云服务被分解成多个服务，每个服务执行不同的数据库操作。最终产生相应的db操作

这种情况下需要单例模式的优点如下：
数据库操作的一致性，即一个操作不应与其他操作发生冲突
优化数据库的各种操作，以提高内存和cpu的利用率
"""

import sqlite3
class MetaSingleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton,cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Databases(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Databases().connect()
db2 = Databases().connect()

print(db1)
print(db2)

"""
当web应用程序对数据库执行某些操作时候，他会多次实例化数据库类，但只创建一个对象，因为只有一个对象，所以对数据库的调用是同步的，此外，这样还能够节约系统资源，并且可以避免消耗过多的内存或cpu

但是如果我们应用是多个web应用共享单个数据库，单例在这种情况下不太好使，因为每增加一个web应用程序，就要新建一个单例，添加一个新的对象来查询数据库，这导致数据库无法同步，并且要耗费大量资源。在这种情况下，数据库链接池比实现单例要好得多
"""
