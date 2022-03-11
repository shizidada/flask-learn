from datetime import datetime

from app import app
from exts import db

from models import User
from models import Article

db.init_app(app)


# 参考数据库操作
# https://blog.csdn.net/weixin_41829272/article/details/80609968

def add_user():
    # user = User(username='鲁迅', password='luxun')
    user = User(username='狮子大大', password='shizidada')
    db.session.add(user)
    db.session.commit()


def delete_user():
    user = User.query.filter(User.username == '狮子大大').first()
    db.session.delete(user)
    db.session.commit()


def update_user():
    user = User.query.filter(User.username == '狮子大大').first()
    user.username = '狮子'
    db.session.commit()


def update_user_all():
    users = User.query.filter(User.username == '狮子').all()
    for index in range(len(users)):
        users[index].username = '狮子' + str(index)
    db.session.commit()


def query_user(username):
    users = User.query.filter(User.username == username).all()
    for user in users:
        print(user)


def add_article():
    article = Article(title='阿Q正传',
                      content='我要给阿Q做正传，已经不止一两年了。...')

    db.session.add(article)
    db.session.commit()


def del_article_by_id(article_id):
    article = Article.query.filter(Article.id == article_id).first()
    db.session.delete(article)
    db.session.commit()


with app.app_context():
    for x in range(10):
        add_user()
    # delete_user()
    # update_user()
    # update_user_all()

    # query_user('狮子大大')

    # del_article_by_id(1)
