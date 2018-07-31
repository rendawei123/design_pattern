import tornado.ioloop
import tornado.web
import sqlite3


class Input(object):
    def __init__(self, val):
        self.val = val

    # 如果对象中有__str__方法，那么在前端显示的时候都显示的是__str__下面的数据
    def __str__(self):
        return '<input type="text" name="n1" value="{0}">'.format(self.val)


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        form_list = [
            Input('alex'),
            Input('tom')
        ]

        self.render('index.html', **{'form_list': form_list})


settings = {
    'template_path': 'templates',
}

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)


def _execute(query):
    """
    对SQLiteBD进行操作
    创建链接
    获取游标对象
    使用游标对象执行事物
    提交查询
    关闭链接
    """
    cx = sqlite3.connect("/Users/David/git/design_pattern/mvc/task.db")
    cu = cx.cursor()
    result = cu.execute(query, ('双龙戏猪', 1))
    cx.commit()
    cx.close()

    return result

if __name__ == "__main__":
    # application.listen(8888)
    # tornado.ioloop.IOLoop.instance().start()

    # query = "select * from task"
    # query = "create table if not exists task(id INTEGER PRIMARY KEY , name TEXT, status NUMERIC)"
    query = "insert into task (name, status) VALUES (?, ?)"
    r = _execute(query)
    print(r)