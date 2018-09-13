#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-31 16:36:57
# @Last Modified by:   anchen
# @Last Modified time: 2018-09-12 13:58:11

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
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime, nullable = False)

    def __init__(self, loginname, name,  telephone, password, sex, interests, job, descr):
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()
        self.loginname = loginname
        self.name = name
        self.sex = sex
        self.interests = interests
        self.job = job
        self.descr = descr
        self.telephone = telephone
        self.password = password


class Catogory(db.Model):
    __tablename__ = 'catogory'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(64), nullable = False, unique = True)
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime)

    def __init__(self, name):
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()
        self.name = name

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(32), nullable = False, unique = True)
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime, nullable = False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(255), nullable = False)
    authorid = db.Column(db.Integer, db.ForeignKey('user.id'))
    catogoryid = db.Column(db.Integer, db.ForeignKey('catogory.id'))
    content = db.Column(db.Text, nullable = False)
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime, nullable = False)

    author = db.relationship('User', backref=db.backref('articles'))
    catogory = db.relationship('Catogory', backref=db.backref('articles'))

    def __init__(self, title, authorid, catogoryid, content):
        self.title = title
        self.authorid = authorid
        self.catogoryid = catogoryid
        self.content = content
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()

class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(64), nullable = False)
    descr = db.Column(db.String(255), nullable = False)
    cover = db.Column(db.String(512), nullable = False)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime, nullable = False)

    user = db.relationship('User', backref=db.backref('albums'))

    def __init__(self, name, descr, cover):
        self.name = name
        self.descr = descr
        self.cover = cover
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()

class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    path = db.Column(db.String(512), nullable = False)
    albumid = db.Column(db.Integer, db.ForeignKey('album.id'))
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime, nullable = False)

    album = db.relationship('Album', backref=db.backref('photos'))

    def __init__(self, path, albumid):
        self.path = path
        self.albumid = albumid
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()

class Emotion(db.Model):
    __tablename__ = 'emotion'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    content = db.Column(db.String(1024), nullable = False)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime, nullable = False)

    user = db.relationship('User', backref = db.backref('emotions'))

    def __init__(self, content):
        self.content = content
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()


