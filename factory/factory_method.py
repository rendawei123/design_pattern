"""
工厂方法模式

假设我们想在不同类型的社交网络上为个人或公司建立简介，而且每个简介都有某些特定的组成章节。在LinkedIn的简介中，有一个章节关于个人申请的专利或出版作品的。在FaceBook上，你将在相册中看到最近度假地点的招聘区，此外，在这两个简介中，都有一个个人信息的区。因此，简而言之，我们要通过将正确的区添加到相应的简介中类创建不同类型的简介。

工厂方法模式的优缺点
1.它具有更大的灵活性，使得代码更加的通用，因为它不是单纯的实例化某个类。这样实现哪些类取决于接口
2.他们是松耦合的，因为创建对象的代码与使用它的代码是分开的。客户端完全不需要关心要传递哪些参数以及实例化哪些类。由于添加新类更加容易，所以降低了维护成本
"""

# 创建一个Selection抽象类来定义一个区是关于哪方面内容的，同时提供一个抽象方法describe()

from abc import ABCMeta,abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    """
    个人部分
    """
    def describe(self):
        print("personal section")

class AlbumSection(Section):
    """
    专辑部分
    """
    def describe(self):
        print("album section")

class PatentSection(Section):
    """
    专利部分
    """
    def describe(self):
        print("Patent section")

class PublicationSection(Section):
    """
    公共部分
    """
    def describe(self):
        print("publication section")

# 我们创建一个名为Profile的抽象类，并提供一个工厂方法，即createProfile()此方法应该由子类来实现，来实际创建带有适当区的简介。
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSections(self, section):
        self.sections.append(section)

class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

if __name__ == '__main__':
    profile_type = input("Which Profile you would like to create? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
