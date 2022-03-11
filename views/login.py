from flask import Blueprint, request, session, render_template, redirect, url_for, g

from models import UserModel

login = Blueprint('login', __name__,
                  static_folder='static',
                  template_folder='templates')


@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login/index.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = UserModel.query.filter_by(telephone=telephone).first()
        try:
            if user and user.check_password(password):
                session['id'] = user.id
                g.user = user
                return redirect(url_for('home.index'))
            else:
                return u'用户名或密码错误！'
        except AttributeError:
            print('登录异常')
        finally:
            print('哈哈哈哈哈哈')
