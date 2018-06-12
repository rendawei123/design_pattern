"""
现在我们写一个基础设施类，即为基础设施提供运营状况监控服务，我们创建一个HealthCheck类，它作为单例实现，我们还要维护一个被监控的服务器列表，当一个服务器从这个列表中删除时，监控软件应该觉察到这一情况，并从被监控的服务器列表中将其删除

为什么这种情况下用单例模式最好？
当添加或删除服务器时，运行状况的检查工作必须由了解基础设施变动情况的同一个对象来完成
"""

class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)

        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")

if __name__ == '__main__':
    hc1 = HealthCheck()
    hc2 = HealthCheck()

    hc1.addServer()
    print("Schedule health check for servers ..")
    for i in range(4):
        print("checking ", hc1._servers[i])

    hc2.changeServer()
    print("Schedule health check for servers ..")
    for i in range(4):
        print("checking ", hc2._servers[i])
