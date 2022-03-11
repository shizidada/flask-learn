from flask import Blueprint, render_template, url_for, request, redirect, jsonify

from exts import db
from forms import RegistForm
from models import UserModel

register = Blueprint('register', __name__)


@register.route('/register', methods=['GET', 'post'])
def index():
    if request.method == 'GET':
        return render_template('register/index.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            # 表单验证成功
            # 保存数据库
            telephone = form.telephone.data
            username = form.username.data
            password = form.password1.data
            user = UserModel(telephone=telephone, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login.index'))
        else:
            return jsonify(form.errors)
