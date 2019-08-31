# coding=utf-8
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define, options
from {{cookiecutter.package_name}}.router import handlers
from {{cookiecutter.package_name}}.config import settings

import {{cookiecutter.package_name}}.models
# 定义一个默认的端口
define("port", default=8000, help="run port ", type=int)

app = tornado.web.Application(handlers, **settings)


def main():
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
