#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-08-31 16:25:39
# @Last Modified by:   anchen
# @Last Modified time: 2018-09-03 12:01:23
from flask import Flask, render_template, request, redirect, session, url_for
from exts import db
import config
from models import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

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
        print(user)
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

@app.context_processor
def get_current_user():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        return {'user': user}
    else:
        return {}



if __name__ == '__main__':
    app.run()