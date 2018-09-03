#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-31 16:36:57
# @Last Modified by:   anchen
# @Last Modified time: 2018-09-03 16:39:00

from exts import db



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    loginname = db.Column(db.String(32), unique = True, nullable = False)
    name = db.Column(db.String(64), nullable = False)
    telephone = db.Column(db.String(11), nullable = False)
    password = db.Column(db.String(127), nullable = False)
    createdate = db.Column(db.Date, nullable = False)
    updatedate = db.Column(db.Date)


class Catogory(db.Model):
    __tablename__ = 'catogory'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(64), nullable = False, unique = True)
    createdate = db.Column(db.Date, nullable = False)
    updatedate = db.Column(db.Date)

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
    authorid = db.Column(db.Integer)
    catogoryid = db.Column(db.Integer)
    content = db.Column(db.Text, nullable = False)
    createdate = db.Column(db.Date, nullable = False)
    updatedate = db.Column(db.Date)

