#!/usr/bin/env python

import os

import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line, define, options

define("host", default='localhost', help="主机地址", type=str)
define("port", default=8000, help="主机端口", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        abc = self.get_argument('arg', '哈哈哈哈哈哈哈哈')
        name = self.get_argument('name', 'Admin')
        sex = self.get_argument('sex', '保密')
        menu = ['红烧肉', '水果沙拉', '糖醋排骨', '牛排', '波士顿龙虾', '三文鱼刺身']
        self.render('index.html', xyz=abc, name=name, sex=sex, menu=menu)


class BlockHandler(tornado.web.RequestHandler):
    def get(self):
        title = '草'
        content = '''
            离离原上草，
            一岁一枯荣，
            野火烧不尽，
            春风吹又生，
            远芳侵古道，
            晴翠接荒城，
            又送王孙去，
            萋萋满别情，
        '''
        self.render('article.html', title=title, content=content)


class StaticTestHandle(tornado.web.RequestHandler):
    def get(self):
        self.render('static_test.html')


def make_app():
    routes = [
        (r"/", MainHandler),
        (r"/block", BlockHandler),
        (r"/tttt", StaticTestHandle)
    ]

    # 获取模版目录和静态文件目录的绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'jingtai')

    return tornado.web.Application(routes,
                                   template_path=template_dir,
                                   static_path=static_dir)


if __name__ == "__main__":
    parse_command_line()

    app = make_app()
    print('server running on %s:%s' % (options.host, options.port))
    app.listen(options.port, options.host)

    loop = tornado.ioloop.IOLoop.current()
    loop.start()