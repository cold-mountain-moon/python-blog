#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-31 16:25:39
# @Last Modified by:   anchen
# @Last Modified time: 2018-09-21 17:58:33
from flask import Flask, render_template, request, redirect, session, url_for, jsonify, g
from exts import db
import config
from models import User, Article,Catogory, Album, Photo, Tag

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

file_server_show = app.config['FILE_SERVER'] + app.config['FILE_SERVER_SHOW']


@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles = articles)

@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        form = request.form
        loginname = form['loginname']
        name = form['name']
        telephone = form['telephone']
        password = form['password']
        confirm = form['confirm-password']
        if password != confirm:
            return render_template('regist.html', loginname = loginname, name = name, telephone = telephone, password = password, confirm_password = confirm, confirm_error = '密码输入不一致')
        else:
            user = User(loginname=loginname, name=name, telephone=telephone, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect('login')

        

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = request.form
        loginname = form['loginname']
        password = form['password']
        user = User.query.filter(User.loginname==loginname, User.password==password).first()
        if user:
            session['user_id'] = user.id
            #session.permanent = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', login_error = '用户名或密码错误', loginname = loginname, password = password)

@app.route('/logout/', methods=['GET'])
def logout():
    #session['user_id'] = None
    #session.pop('user_id')
    #del session['user_id']
    session.clear()
    return redirect(url_for('login'))

@app.route('/catogory/article/<catogoryid>')
def article_list(catogoryid):

    articles = Article.query.filter(Article.catogoryid==catogoryid)
    return render_template('article/list.html', articles=articles)

@app.route('/article/<id>', methods=['GET'])
def article_detail(id):
    article = Article.query.filter(Article.id == id).first()
    return render_template('article/detail.html', article=article)

@app.route('/album/', methods = ['GET'])
def album_list():
    albums = Album.query.all()
    return render_template('album/list.html', albums = albums, file_server=file_server_show)

@app.route('/album/photo/<id>')
def album_photo_list(id):
    photos = Photo.query.filter(Photo.albumid == id)
    return render_template('photo/list.html', photos = photos)

@app.route('/message/board/', methods = ['GET', 'POST'])
def message_board_list():
    if request.method == 'GET':
        return render_template('messageboard/list.html')
    else:
        form = request.form
        
        return jsonify({"error": 0, "msg": '评论成功!'})


@app.context_processor
def every_request():
    result = {'main_catogories': g.main_catogories, 'tags_cloud': g.tags_cloud, 'article_catogories': g.article_catogories}
    user_id = session.get('user_id')

    if user_id:
        user = User.query.filter(User.id == user_id).first()
        result['user'] = user
    return result

@app.before_request
def first_request():
    if not hasattr(g, 'main_catogories'):
        catogories = Catogory.query.order_by('order').all()
        setattr(g, 'main_catogories', catogories)
    if not hasattr(g, 'tags_cloud'):
        tags = Tag.query.all()
        setattr(g, 'tags_cloud', tags)
    if not hasattr(g, 'article_catogories'):
        article_catogories = Catogory.query.filter(Catogory.route=='article_list')
        setattr(g, 'article_catogories', article_catogories)





if __name__ == '__main__':
    app.run(threaded=True)