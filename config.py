#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-31 16:25:49
# @Last Modified by:   anchen
# @Last Modified time: 2018-08-31 16:31:53
import os

SECRET_KEY = os.urandom(24)

DEBUG = True

DIALECT='mysql'
DRIVER='mysqlconnector'
USERNAME='root'
PASSWORD='root'
HOST='127.0.0.1'
PORT='3306'
DATABASE='blog-db'

SQLALCHEMY_DATABASE_URI='{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
