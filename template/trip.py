"""
现在以旅行社的案例来理解现实世界中的模版方法模式

一个旅行社定义了各种旅游路线，并提供度假套装行程。
一个行程套餐本质上是你作为客户允诺的一次旅行。旅行还涉及一些详细信息，如游览地点，交通方式和与旅行有关的其他因素。
当然，同样的行程可以根据客户的需求进行不同的定制
"""

from abc import ABCMeta, abstractmethod


class Trip(metaclass=ABCMeta):
    """
    抽象对象，他是一个接口，定义了不同日子使用的交通方式和参观的地点等细节
    """
    @abstractmethod
    def set_transport(self):
        """
        设置交通方式
        """
        pass

    @abstractmethod
    def day1(self):
        """
        特定日期所参观的地点
        """
        pass

    @abstractmethod
    def day2(self):
        """
        特定日期所参观的地点
        """
        pass

    @abstractmethod
    def day3(self):
        """
        特定日期所参观的地点
        """
        pass

    @abstractmethod
    def return_home(self):
        """
        回家
        """
        pass

    def itinerary(self):
        """
        行程，模板方法创建完整的行程（即算法，在本例中为旅行）。旅行的序列为，首先定义交通模式，然后是每天要参观的地点，以及回家
        """
        self.set_transport()
        self.day1()
        self.day2()
        self.day3()
        self.return_home()


class VeniceTrip(Trip):
    """
    威尼斯旅行
    """
    def set_transport(self):
        print("Take a boat and find your way in the Grand Canal")  # 乘船，在大运河找到自己的路

    def day1(self):
        print("Visit St Mark s Basilica in St Mark s Square")

    def day2(self):
        print("Appreciate Dogs is Palace")

    def day3(self):
        print("Enjoy the food near the Rialto Bridge")

    def return_home(self):
        print("Get souvenirs for friends and get back")


class MaldivesTrip(Trip):
    """
    马尔代夫旅行
    """
    def set_transport(self):
        print("On foot, on any island, Wow!")

    def day1(self):
        print("Enjoy the marine life on Banana Reef")

    def day2(self):
        print("Go for the water sports and snorkelling")   # 浮潜

    def day3(self):
        print("Relax on the beach and enjoy the sun")

    def return_home(self):
        print("Dont feel like leaving the beach..")


class TravelAgency:
    """
    旅行社
    """
    def arrange_trip(self):
        """
        让用户选择历史旅行或海滩旅行
        """
        choice = input("What kind of place you would like to go historical or to a beach?")
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()


if __name__ == '__main__':
    TravelAgency().arrange_trip()
