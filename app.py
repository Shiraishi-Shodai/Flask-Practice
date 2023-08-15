# !/usr/bin/env python3
# -*- coding:utf-8 -*-


from flask import Flask, render_template,request
import flask

app = Flask(__name__, template_folder='template')
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return 'UserName: ' + str(username)

@app.route('/p-test', methods=['POST'])
def ptest():
    if request.method == 'POST':  
        name = request.form['name']
        return f'こんにちは{name}さん'
    
@app.route('/myapp')
def mypage():
    login = True
    if login is False:
        return flask.jsonify({
            'code' : 400,
            'msg' : 'Bad Request'
        })
        
    user_data = {'username': 'ai_academy'}
    return flask.jsonify({
        'code' : 200,
        'msg' : 'DK',
        'result': user_data
    })
    
if __name__ == '__main__':
    app.run(port=8000, debug=True)

