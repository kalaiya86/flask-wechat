#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-06 10:11:43
# @Author  : Kelly (weiqin.wang_c@chinapnr.com)
# @Link    : ${link}
# @Version : $Id$

import os

def setDir(dirs=''):
    path_tmp = os.path.join(dirs, 'tmp')
    os.mkdir(path_tmp)
    path_app = os.path.join(dirs, 'app')
    os.mkdir(path_app)
    path_static = os.path.join(path_app, 'static')
    os.mkdir(path_static)
    path_templates = os.path.join(path_app, 'templates')
    os.mkdir(path_templates)
    # config文件
    config = ['DEBUG = False']
    file_config = os.path.join(dirs, 'config.py')
    # a追加模式w覆盖模式
    f = open(file_config, mode='a', encoding="UTF-8")
    for c in config:
        f.write(c + "\n")
    f.close()
    # run文件
    config_run = '''#!flask/bin/python
from app import app

if __name__ == "__main__":
    app.debug = app.config['DEBUG']
    app.run()
'''
    file_run = os.path.join(dirs, 'run.py')
    f = open(file_run, mode='a', encoding="UTF-8")
    f.write(config_run)
    f.close()
    # app init
    config2 = '''from flask import Flask

app = Flask(__name__)
from app import views
'''
    file_app = os.path.join(path_app, '__init__.py')
    f = open(file_app, mode="w", encoding="UTF-8")
    f.write(config2)
    f.close()

    # app view
    config3 = '''from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
'''
    file_app = os.path.join(path_app, 'views.py')
    f = open(file_app, mode="w", encoding="UTF-8")
    f.write(config3)
    f.close()

setDir()