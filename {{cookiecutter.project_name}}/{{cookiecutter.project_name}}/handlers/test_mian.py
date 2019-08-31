import tornado.web
from {{cookiecutter.package_name}}.handlers.base.base_handler import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        self.write("hello word")
        # 这个可以返回json 数据已经设置好返回头了
