#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2020年2月7日

@author: jianzhihua
'''


from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_app import main_app
from flask_script import Manager
from flask_migrate import MigrateCommand

manager = Manager(main_app)
manager.add_command('db', MigrateCommand)

db = SQLAlchemy(main_app)
session = db.session
migrate = Migrate(main_app, db)
