#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-30 17:35:48
# @Last Modified by:   anchen
# @Last Modified time: 2018-08-30 18:13:23
import os
from flask import Flask

def create_app(test_config=None):
    # instance_relative_config=True告诉应用，配置文件是相对于instance folder
    # 的相对路径。实例文件夹在本包的外面，用于存放本地数据（如配置秘钥和数据库等）
    app = Flask(__name__, instance_relative_config=True)
    # 设置应用的缺省配置：
    # SECRET_KEY是Flask保证数据安全的，为方便设置为'dev'，在发布的时候应该使用一
    # 个随机值来重载它
    # DATABASE:指定数据库文件的存放路径。位于Flask用于存放实例的app.instance_path
    # 之内
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path, 'blog.mysql'),
    )
    if test_config is None:
        # 用config.py中的值重载缺省配置，例如正式环境中设置正式的SECRET_KEY
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        # 确保app.instance_path存在，因为Flask不会自动创建实例文件夹，但是必须保证
        # 该目录存在，因为数据库文件会保存在这里
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/'):
        return u'应用首页'

    return app