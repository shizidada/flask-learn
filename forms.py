import wtforms
from wtforms import validators


class RegistForm(wtforms.Form):
    telephone = wtforms.StringField(
        validators=[
            validators.length(min=11, max=11, message=u'请输入正确手机号码')
        ]
    )
    username = wtforms.StringField(
        validators=[
            validators.InputRequired(message=u'请输入用户名')
        ]
    )
    password1 = wtforms.StringField(
        validators=[
            validators.InputRequired(message=u'请输入密码')
        ]
    )
    password2 = wtforms.StringField(
        validators=[
            # validators.InputRequired(),
            validators.EqualTo('password1', message='两次密码输入不一致')
        ]
    )
