"""
现在以安装向导的例子来实现命令模式

通常，安装意味着需要根据用户作出的选择来复制或移动文件系统中的文件。
在下面的示例中，我们首先在呼呼段代码中创建Wizard对象，然后使用preferences()方法存储用户在向导的各个屏幕期间作出的选择。
在安装向导中单机Finish按钮时，就会调用execute()方法，之后execute()方法将会根据首选项来开始安装
"""


class Wizard:
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.rootdir)
            else:
                print("no operation")


if __name__ == '__main__':
    # 客户端
    wizard = Wizard('python3.5.gzip', '/user/bin/')
    # 安装向导选择
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    # 点击完成开始安装
    wizard.execute()