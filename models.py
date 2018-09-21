#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-31 16:36:57
# @Last Modified by:   anchen
# @Last Modified time: 2018-09-21 17:54:22

import datetime
from exts import db



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    loginname = db.Column(db.String(32), unique = True, nullable = False)
    name = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(32))
    roletype = db.Column(db.String(1), nullable = False)
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
    order = db.Column(db.Integer)
    route = db.Column(db.String(127), nullable = False)
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime)

    def __init__(self, name, order=0, route='index'):
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()
        self.route = route
        self.order = order
        self.name = name

article_tag = db.Table('article_tag',
    db.Column('articleid', db.Integer, db.ForeignKey('article.id'), primary_key = True),
    db.Column('tagid', db.Integer, db.ForeignKey('tag.id'), primary_key = True)
)

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(32), nullable = False, unique = True)
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime, nullable = False)

    def __init__(self, name):
        self.name = name
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()


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
    tags = db.relationship('Tag', secondary='article_tag', backref=db.backref('articles'))

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

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # 类型： 1(文章评论)， 2(留言)
    commenttype = db.Column(db.String(1), nullable = False)
    articleid = db.Column(db.Integer, db.ForeignKey('article.id'))
    content = db.Column(db.String(1024), nullable = False)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime, nullable = False)

    article = db.relationship('Article', backref = db.backref('comments'))
    user = db.relationship('User', backref = db.backref('comments'))

    def __init__(self, commenttype, content):
        self.content = content
        self.commenttype = commenttype
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()


class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    content = db.Column(db.String(1024), nullable = False)
    commentid = db.Column(db.Integer, db.ForeignKey('comment.id'))
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    createdate = db.Column(db.DateTime, nullable = False)
    updatedate = db.Column(db.DateTime, nullable = False)

    comment = db.relationship('Comment', backref = db.backref('replies'))

    def __init__(self, content):
        self.content = content
        self.createdate = datetime.datetime.now()
        self.updatedate = datetime.datetime.now()

