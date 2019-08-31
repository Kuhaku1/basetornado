# coding=utf-8
import tornado.escape
import tornado.websocket
import tornado.web
from {{cookiecutter.package_name}}.libs.db.dbsession import dbSession


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = dbSession

    def on_finish(self):
        self.db.close()

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')
