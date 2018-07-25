"""
下面例子为现实世界中的代理模式：
我们通过付款用例来展示代理模式的现实应用场景。

假设你在商场看中来一件衣服，想买但是手里的先进却不够用了，所以你在商场中就需要刷卡，这笔钱就会划入商家的账户，完成支付
"""

from abc import ABCMeta, abstractclassmethod


class You:
    """
    你的行为
    """
    def __init__(self):
        """
        调用代理，并将其实例化
        """
        print("You: Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        """
        在内部调用代理的方法进行付款
        :return:
        """
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        """
        如果付款成功，返回此方法
        """
        if self.isPurchased:
            print("You: Wow! Denim shirt is Mine")
        else:
            print("You: I should earn more")


class Payment(metaclass=ABCMeta):
    """
    主题是，主题是由代理和真实主题实现的接口，他是一个抽象类
    """
    @abstractclassmethod
    def do_pay(self):
        """
        此方法需要借助代理和真实主题来实现
        """
        pass


class Bank(Payment):
    """
    真实主题，银行类
    实际完成从你的账户向商家账户划账的工作
    """
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        """
        Bank的私有方法，用来获取借记卡持有人的账户详细信息，为来方便起见，我们强制使用与账号相同的借记卡
        """
        self.account = self.card
        return self.account

    def __hasFunds(self):
        """
        查看账户持有人在账户中是否有足够的资金来为衬衫付款
        """
        print("Bank: Checking if Account", self.__getAccount(), "has enough funds")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        """
        负责根据可用资金向商家付款
        :return:
        """
        if self.__hasFunds():
            print("Bank: Paying the merchant")
            return True
        else:
            print("Bank: Sorry, not enough funds!")
            return False


class DebitCard(Payment):
    """
    真实主题的代理
    """
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        """
        当你需要付款时，调用此方法
        """
        card = input("Proxy: Punch in Card Number:")
        self.bank.setCard(card)
        return self.bank.do_pay()


if __name__ == '__main__':
    you = You()
    you.make_payment()
