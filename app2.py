# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
app2 = Flask(__name__, template_folder='template')

@app2.route('/')
def hello_world():
    return "<h1>Hello</h1>"

@app2.route('/<name>')
def hello_user(name):
    return f'Hello{name}'

items = [
    'アイテム1',
    'アイテム2',
    'アイテム3',
    'アイテム4',
    'アイテム5',
    'アイテム6',
    'アイテム7',
]

@app2.route('/list')
def hello():
    return render_template('app2.html', items=items)

di = [
    {'name1': 'Miura', 'name2': 'Junya'},
    {'name1': 'Tanaka', 'name2': 'Taro'},
]
@app2.route('/di')
def hello2():
    return render_template('app2.html', di=di)

if __name__ == '__main__':
    app2.run(port=8000,debug=True)