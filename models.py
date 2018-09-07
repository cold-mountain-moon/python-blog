#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-31 16:36:57
# @Last Modified by:   anchen
# @Last Modified time: 2018-09-07 15:06:09

import datetime
from exts import db



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    loginname = db.Column(db.String(32), unique = True, nullable = False)
    name = db.Column(db.String(64), nullable = False)
    telephone = db.Column(db.String(11), nullable = False)
    password = db.Column(db.String(127), nullable = False)
    sex = db.Column(db.String(1), nullable = False)
    interests = db.Column(db.String(127), nullable = False)
    portrait = db.Column(db.LargeBinary)
    job = db.Column(db.String(32), nullable = False)
    descr = db.Column(db.Text, nullable = False)
    createdate = db.Column(db.Date, nullable = False)
    updatedate = db.Column(db.Date)

    def __init__(self, loginname, name,  telephone, password):
        self.createdate = datetime.datetime.now()
        self.loginname = loginname
        self.name = name
        self.telephone = telephone
        self.password = password


class Catogory(db.Model):
    __tablename__ = 'catogory'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(64), nullable = False, unique = True)
    createdate = db.Column(db.Date, nullable = False)
    updatedate = db.Column(db.Date)

    def __init__(self, name):
        self.createdate = datetime.datetime.now()
        self.name = name

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(32), nullable = False, unique = True)
    createdate = db.Column(db.Date, nullable = False)
    updatedate = db.Column(db.Date)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(255), nullable = False)
    authorid = db.Column(db.Integer, db.ForeignKey('user.id'))
    catogoryid = db.Column(db.Integer, db.ForeignKey('catogory.id'))
    content = db.Column(db.Text, nullable = False)
    createdate = db.Column(db.Date, nullable = False)
    updatedate = db.Column(db.Date)

    author = db.relationship('User', backref=db.backref('articles'))
    catogory = db.relationship('Catogory', backref=db.backref('catogories'))

    def __init__(self, title, authorid, catogoryid, content):
        self.title = title
        self.authorid = authorid
        self.catogoryid = catogoryid
        self.content = content
        self.createdate = datetime.datetime.now()


