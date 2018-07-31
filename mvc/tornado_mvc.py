"""
现在我们用Tornado Web用用程序框架来开发一个单页面应用程序。这个程序用于管理用户的各种任务，
同时用户还具有添加任务、更新任务和删除任务的权限。

1. 让我们先从控制器开使。在Tornado中，控制器被定义为视图/应用程序路由。
我们需要定义多个视图，例如列出任务、创建任务、关闭任务以及在无法处理请求时的操作

2. 我们还应该定义模型，即列出、创建或删除任务的数据库操作

3. 视图由Tornado中的模板显示。对于应用程序来说，我们需要一个模板来显示、创建或删除任务，以及另一个模板用于没有找到URL的情形
"""

import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3

"""
模型
"""


def _execute(query, string=None):
    """
    对SQLiteBD进行操作
    创建链接
    获取游标对象
    使用游标对象执行事物
    提交查询
    关闭链接
    """
    # result_dict = {"1":'1'}
    result_dict = []
    cx = sqlite3.connect("/Users/David/git/design_pattern/mvc/task.db")
    cu = cx.cursor()
    if string:
        cu.execute(query, string)
    else:
        result = cu.execute(query)
        for i in result:
            result_dict.append(i)
    cx.commit()
    cx.close()

    return result_dict


class IndexHandler(tornado.web.RequestHandler):
    """
    返回存储在数据库中的所有任务。它返回一个与关键任务有关的字典。
    它执行select数据库操作来获取这些任务。
    """
    def get(self, *args, **kwargs):
        query = "select * from task"
        todo = _execute(query)
        self.render("index1.html", todos=todo)
        # self.render("1.html", todos=todo)
        # self.write('hello word')


class NewHandler(tornado.web.RequestHandler):
    """
    添加任务。它检查是否有一个POST调用来创建一个新任务，并在数据库中执行insert操作
    """
    def get(self, *args, **kwargs):
        self.render("new1.html")

    def post(self, *args, **kwargs):
        name = self.get_argument('name', None)
        query = "create table if not exists task" \
                " (id INTEGER PRIMARY KEY , name TEXT, status NUMERIC)"

        _execute(query)

        query = "insert into task (name, status) VALUES (?, ?)"
        string = (name, 1)
        _execute(query, string)
        self.redirect('/')


class UpdateHandler(tornado.web.RequestHandler):
    """
    在将任务标记为完成或者重新打开给定任务时非常有用。在这种情况下，将执行UPDATE数据库操作，
    将任务的状态设置为open/closed
    """
    def get(self, id, status):
        query = "update task set status=? WHERE id=?"
        string = (int(status), id)
        _execute(query, string)
        self.redirect('/')


class DeleteHandler(tornado.web.RequestHandler):
    """
    这将从数据库中删除制定任务。一旦删除，任务将会从任务列表中消失
    """
    def get(self, id):
        query = "delete from task WHERE id=?"
        string = id
        _execute(query, string)
        self.redirect('/')


"""
视图为templates目录下的html文件

下面为控制器
"""


class RunApp(tornado.web.Application):
    """
    应用程序路由，相当于控制器
    """
    def __init__(self):
        Handlers = [
            (r'/', IndexHandler),  # 列出所有任务
            (r'/todo/new', NewHandler),  # 创建新任务
            (r'/todo/update/(\d+)/(\d+)', UpdateHandler),  # 将任务状态更新为打开或关闭
            (r'/todo/delete/(\d+)', DeleteHandler)  # 删除已完成任务
        ]

        settings = dict(
            debug=True,
            template_path="templates",
            static_path="static",
        )

        tornado.web.Application.__init__(self, Handlers, **settings)


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
