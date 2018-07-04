"""
现在让我们来举例说明门面模式

假设你要在家中举行一场婚礼，你必须要预定一家酒店或场地，与餐饮人员交代酒菜，布置场景、并安排北京音乐

现在从门面模式的角度类看待这些事情
客户端：你需要在婚礼前及时完成所有的准备工作
门面：会务经理负责与所有相关人员进行交涉，这些人员负责处理食物、花卉装饰等
子系统：他们代表提供餐饮、酒店管理和花卉装饰等服务的系统
"""

class EventManager(object):
    """
    门面类,简化接口
    """
    def __init__(self):
        print("Event Manager: Let me talk to the folks")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()  # 花商
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()  # 餐饮服务商
        self.caterer.setCuisine()

class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")
    def __isAvaliable(self):
        print("Is the Hotel free for the event on given day?")
        return True
    def bookHotel(self):
        if self.__isAvaliable():
            print("Registered the Booking\n\n")

class Florist(object):
    def __init__(self):
        print("Flower Decorations for the event? --")
    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would bo used for Decorations\n\n")

class Caterer(object):
    def __init__(self):
        print("Food Arrangement for the Event")
    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")

class You(object):
    def __init__(self):
        print("You::Whoa!Marriage Arrangements??!!!")
    def askEventManager(self):
        print("You::Let is Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You::Thanks to Event Manager, all preparations done! Phew!")

if __name__ == '__main__':
    you = You()
    you.askEventManager()
