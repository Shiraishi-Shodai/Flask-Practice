from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="template")
# データベースのURL
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Test.db"
# データベースの変更を追跡(メモリを消費する)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# SQL分のログを出力
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

class Shohin(db.Model):
    __tablename__ = "Shohin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Integer)

    def __init__(self, id, name, price) -> None:
        self.id = id
        self.name = name
        self.price = price

# @app.before_first_requestのデコレータは最初のrequestの時だけデコレートしている関数を実行します
# @app._got_first_request
# def init():
#     print('通貨しました')
#     # テーブルを作成
#     db.create_all()
#     return "テーブルを作成しました"

@app.route('/')
def index():
    # init()
    return "テーブルを作成しました"

@app.route('/result', methods=["GET", "POST"])
def insert():
    # shohin = Shohin(id=1, name="トイレットペーパー", price=600)
    # db.session.add(shohin)
    # db.session.commit()

    # shohin = db.session.query(Shohin).all()
    shohin = db.session.query(Shohin).filter_by(id=1).first()
    print(f'結果{shohin}')
    return render_template('index.html', shohin=shohin)



if __name__ == "__main__":
    app.run()