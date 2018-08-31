#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-31 16:37:06
# @Last Modified by:   anchen
# @Last Modified time: 2018-08-31 16:43:41
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand
from python_blog import app
from exts import db

manager = manager(app)
migrate = Migrate(app, db)

migrate.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()