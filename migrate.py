#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-31 16:37:06
# @Last Modified by:   anchen
# @Last Modified time: 2018-09-03 16:33:55
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand
from python_blog import app
from exts import db
from models import User, Catogory, Tag, Article

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()