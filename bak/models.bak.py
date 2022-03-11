from datetime import datetime

from exts import db


# 用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_time = db.Column(db.DateTime, nullable=False, default=datetime.now)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


# 一对多
# 一个 School 对应多个 Student
# 表示一对多的关系时，在子表类 Student 中需要通过 foreign key (外键)引用父表类 School
class School(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    teachers = db.relationship("Teacher", backref=db.backref('teachers'), lazy='dynamic')


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String(255))

    # 设置连接 Teacher 的并反向查询 School
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))  # , nullable=False
