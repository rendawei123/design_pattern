"""
假设想为ios设备开发自己的交叉编译器

首先开发一个抽象类（编译器），来定义编译器的算法。
编译器执行的操作是收集由程序语言编写的源代码，然后编译成目标代码（二进制格式）。
我们将这些步骤定义为collect_source()和compile_to_object()抽象方法，同时还定义来负责执行程序的run()方法。
该算法是由compile_and_run()方法来定义的，他通过内部调用来定义编译器的算法

然后，让具体类IosCompiler实现抽象方法，在ios设备上编译并运行swift代码
"""

from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    """
    抽象类，来定义编译器的算法
    """
    @abstractmethod
    def collect_source(self):
        """
        收集由程序语言编写的源代码
        """
        pass

    @abstractmethod
    def compile_to_object(self):
        """
        编译成目标代码（二进制格式）
        """
        pass

    @abstractmethod
    def run(self):
        """
        执行程序
        """
        pass

    def compile_and_run(self):
        """
        编译器算法
        """
        self.collect_source()
        self.compile_to_object()
        self.run()


class IosCompiler(Compiler):
    """
    ios编译器定义
    """
    def collect_source(self):
        print("Collecting Swift Source Code")

    def compile_to_object(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program running on runtime environment")


if __name__ == '__main__':
    ios = IosCompiler()
    ios.compile_and_run()
