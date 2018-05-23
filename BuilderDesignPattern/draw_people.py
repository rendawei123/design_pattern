"""
建造者模式：

将一个复杂对象的构建和表示分离，使得同样的构建过程可以创建不同的表示，我们想要创建一个由多个部分构成的对象，而且他的构成需要一步接一步的完成，只有当各个部分都创建好，这个对象才算是完整的。这正是建造者设计模式（Builder design
pattern）的用武之地。建造者模式将一个复杂对象的构造过程与其表现分离，这样，同一个构造
过程可用于创建多个不同的表现
"""
from abc import abstractmethod, ABCMeta

class Builder(metaclass=ABCMeta):
    """
    建造者
    """
    @abstractmethod
    def draw_arm(self):
        pass

    @abstractmethod
    def draw_foot(self):
        pass

    @abstractmethod
    def draw_head(self):
        pass

    @abstractmethod
    def draw_body(self):
        pass


class ThinGirl(Builder):
    """
    瘦女孩
    """
    def draw_arm(self):
        print("画手")

    def draw_foot(self):
        print("画脚")

    def draw_head(self):
        print("画头")

    def draw_body(self):
        print("画瘦身体")


class FatGirl(Builder):
    """
    胖女孩
    """
    def draw_arm(self):
        print("画手")

    def draw_foot(self):
        print("画脚")

    def draw_head(self):
        print("画头")

    def draw_body(self):
        print("画胖身体")


class Director():
    """
    指挥者
    """
    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.draw_arm()
        self.person.draw_foot()
        self.person.draw_head()
        self.person.draw_body()


if __name__ == '__main__':
    thin = ThinGirl()
    fat = FatGirl()
    director_thin = Director(thin)
    director_thin.draw()
    director_fat = Director(fat)
    director_fat.draw()
