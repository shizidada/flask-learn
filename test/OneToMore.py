from app import app
from exts import db

from models import School
from models import Teacher

db.init_app(app)


def add():
    # school = School(name='希望中學')
    # t1 = Teacher(name='张三', age=26, job='语文')
    # t2 = Teacher(name='李斯特', age=24, job='英语')
    # t3 = Teacher(name='艾贝', age=23, job='英语')
    # t4 = Teacher(name='科比', age=22, job='体育')
    # t5 = Teacher(name='项守临', age=32, job='数学')
    # school.teachers = [t1, t2, t3, t4, t5]
    #
    # school2 = School(name='实验中學')
    # t11 = Teacher(name='熊乐快', age=22, job='数学')
    # t22 = Teacher(name='穆钱肯', age=34, job='英语')
    # t33 = Teacher(name='朱无身', age=23, job='英语')
    # t44 = Teacher(name='任止室', age=26, job='语文')
    # t55 = Teacher(name='姚希察', age=39, job='体育')
    # school2.teachers = [t11, t22, t33, t44, t55]
    #
    # db.session.add(school)
    # db.session.add(school2)
    # db.session.commit()

    # school = School(name='古天乐中學')
    t1 = Teacher(name='李斯特', age=24, job='英语')
    # school.teachers = [t1]

    db.session.add(t1)
    db.session.commit()


def select():
    schools = School.query.all()
    for school in schools:
        for t in school.teachers.filter(Teacher.job == '体育'):
            print(t.name)


def select_teacher_by():
    teacher = Teacher.query.filter(Teacher.id == 1).first()
    school = School.query.filter(School.id == teacher.s_id).first()
    print(school.name)


with app.app_context():
    add()
    # select()
    # select_teacher_by()
