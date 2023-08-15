# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy #ORマッパー
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
import json

app = Flask(__name__, template_folder='template')
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
    'user':'root',
    'password' : 'pathSQL',
    'host': 'localhost',
    'db_name': 'data4'
})

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Memo(db.Model):
    __tablename__ = 'memos'

    id = db.Column('id', INTEGER(11), primary_key=True)
    memo = db.Column('memo', VARCHAR(255), nullable=True)
    
# with app.app_context():
#     # テーブルを作成
#     db.create_all()

@app.route('/')
def index():
    return render_template('dbIndex.html')

@app.route('/insert', methods=['POST'])
def insert():                       #memosテーブルに行を挿入
    if request.method == 'POST':
        memo_text = request.form['memo']
        memo = Memo(memo=memo_text)
        db.session.add(memo)
        db.session.commit()
        return render_template('dbResult.html')
    
@app.route('/select')
def select():   #テーブル一覧をリスト型で取得し送信
    memos = Memo.query.all()
    return render_template('dbResult2.html', memos=memos)

if __name__ == '__main__':
    app.run(port=8000, debug=True)