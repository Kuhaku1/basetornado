# coding=utf-8
from {{cookiecutter.package_name}}.libs.db.dbsession import Base
from {{cookiecutter.package_name}}.libs.db.dbsession import engine
# 创建表
from .user_model import user_model

Base.metadata.create_all(engine)
